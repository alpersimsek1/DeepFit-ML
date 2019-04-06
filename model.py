from pyspark.sql import Row
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName('abc').getOrCreate()
ratingDS = spark.read.csv("finalRatings.csv").selectExpr("_c0 as userId", "_c1 as foodName", "_c2 as rating").select("userId",
                                                                                                               "foodName",
                                                                                                               "rating")
ratingDS.show()
food_names = ["id", "item"]

foodDS = pd.read_csv("/Users/alper.simsek/Bitirme/DeepFit-ML/items.tsv", sep='\t', na_values="0.00", comment='\t',
                     names=food_names, skipinitialspace=True, error_bad_lines=False)
spliter = lambda x: x.split('__')[-1:][0]
foodDS["item"] = foodDS["item"].apply(spliter).to_frame()
finalDS = foodDS.drop_duplicates(subset=['item'])
postgre = spark.createDataFrame(finalDS)
postgre.show()
ta = ratingDS.alias('ta')
tb = postgre.alias('tb')

inner_join = ta.join(tb, ta.foodName == tb.item, how="left").select("userId", "foodName", "rating", "id")

newDS = spark.createDataFrame(
    inner_join.rdd.map(lambda p: Row(userId=int(p[0]), foodName=p[1], rating=int(p[2]), id=int(p[3]))))
newDS.show()

als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="id", ratingCol="rating",
          coldStartStrategy="drop")
(training, test) = newDS.randomSplit([0.8, 0.2])

model = als.fit(training)
predictions = model.transform(test)
userRecs = model.recommendForAllUsers(10)
pandas_user_recs = userRecs.toPandas()

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/Users/alper.simsek/Bitirme/DeepFit-ML/database/ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
userRecs.show()


def take_food_ids(l):
    arr = []
    for i in l:
        arr.append(str(i[0]))
    return arr


apply_mapping_foods = lambda list_of_foods: take_food_ids(list_of_foods)

pandas_user_recs['recommendations'] = pandas_user_recs['recommendations'].apply(apply_mapping_foods)

for index, food in pandas_user_recs.iterrows():
    doc_ref2 = db.collection(u'food_preferences').document(str(food['userId']))
    doc_ref2.set({
        u'user_id': str(food['userId']),
        u'preferences': food['recommendations']
    })
    print(str(food['userId']) + " written to the food preferences" )
