### This project is for Final Design Project of Computer Engineering (Koc University) 
This is a college project, so this is not commercial

### Using Pandas and Apache Spark (pyspark) to create food recommendation systems. 
We used Apache Sparks ALS matrix factorization to recommend foods to the users. 

We had to manipulate the datasets to create a model which will be useful to us. 

The base datasets are data.tsv and items.tsv. 


#### manipulating and analyzings these datasets we created our own datasets;
finalRatings.csv -> which contains user ratings. 

finalData.csv 

allData.json folder contains all data. 

menu.py reads menu.json contains which food most consumed by another foods. 

#### model can be found in the model.py file. 

After creating the recommendations and sample menu we send them to the Firebase Firestore Admin SDK to use in our Android Application. 

ServiceAccountKey.json is needed if the code runs on local machine. But don't need that key in Google Cloud Platform. 
Also we use GCP to train our model. 

### The dataset we are using can be found on the internet;
This dataset contains 1.9 million meals logged by 9.8K MyFitnessPal users on 71K food items from September 2014 through April 2015. Food items with similar textual description have been grouped together.

The dataset consists of data and item files. Their formats are described below.

data.tsv: 
Each line is a tab separated list of meal_id, user_id, date, meal_sequence, and food_ids. It describes a list of food items consumed by a user in a meal each day. The meal_sequence field indicates the ordering of the meal on a particular day, e.g., meal_sequence = 1 is the first meal of the day.

items.tsv:
A list of food tem IDs and names separated by tab. Each food name is represented by a comma-separated list of salient features where each salient feature consists of a triplet of food and cooking releated words separated by double underscores. E.g., egg_dairy__dairy_product__milk is a salient feature of (egg, dairy product, milk) triplet.

If you use the dataset in scientific publication, a citation to the following paper would be greatly appreciated:

- Achananuparp, P. and Weber, I. (2016) Extracting Food Substitutes From Food Diary via Distributional Similarity. In Proceedings of the International Workshop on Engendering Health with RecSys (HealthRecSys2016).
