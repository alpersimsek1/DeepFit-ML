import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('abc').getOrCreate()

url = "data.tsv"
col_names_mfp = ["meal_id",	"user_id", "date",	"meal_sequence", "food_ids"]
food_names = ["id","item"]
dataset = pd.read_csv(url, sep='\t', na_values = "0.00", comment='\t', names=col_names_mfp, skipinitialspace=True, error_bad_lines=False,usecols=['food_ids', 'user_id'])

foodDS = pd.read_csv("items.tsv", sep='\t', na_values = "0.00", comment='\t', names=food_names, skipinitialspace=True, error_bad_lines=False)

spliter = lambda x: x.split('__')
foodDS["item"] = foodDS["item"].apply(spliter).to_frame()
commaSplitter = lambda x: x.split(',')
dataset["food_ids"] = dataset["food_ids"].apply(commaSplitter).to_frame()
count = 0

def map_foods(l):
    global count
    print(str(count))
    count = count + 1
    for i in range(0,len(l)):
        l[i] = foodDS[foodDS["id"]==int(l[i])]["item"].values[0]
    return l

apply_mapping_foods = lambda list_of_foods: map_foods(list_of_foods)

newDS3 = dataset
newDS3["food_ids"] = newDS3["food_ids"].apply(apply_mapping_foods)
# newDS.head(1000).to_csv("finalData.csv")

finalDS = newDS3

def take_last_of_list(l):
    new_l = []
    for x in l:
         new_l.append(x[-1:][0])
    return new_l

take_last_apply = lambda x: take_last_of_list(x)

finalDS["food_ids"] = finalDS["food_ids"].apply(take_last_apply)
df2 = spark.createDataFrame(finalDS)
df2.coalesce(1).write.format('json').save('all_data.json')
