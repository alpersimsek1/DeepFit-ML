from pyspark.sql import SparkSession
import firebase_admin
from firebase_admin import credentials, firestore

spark = SparkSession.builder.appName('sample_menu').getOrCreate()
menuDS = spark.read.json("/Users/alper.simsek/Bitirme/DeepFit-ML/best_20_food/menu.json")
pandas_user_recs = menuDS.toPandas()

cred = credentials.Certificate("/Users/alper.simsek/Bitirme/DeepFit-ML/database/ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def apply(l):
    return l[0:10]

apply_to_df = lambda s: apply(s)
pandas_user_recs['prefs'] = pandas_user_recs['prefs'].apply(apply_to_df)

doc_ref2 = db.collection(u'sample_menu').document(str("sample"))
doc_ref2.set({
    u'keys': pandas_user_recs.to_dict()
})

# for index, food in pandas_user_recs.iterrows():
#     doc_ref2 = db.collection(u'sample_menu').document(str(food['key']))
#     doc_ref2.set({
#         u'preferences': food['prefs'][0:30]
#     })
#     print(str(food['key']) + " written to the sample menu")
