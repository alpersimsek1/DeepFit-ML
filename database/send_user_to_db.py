import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

cred = credentials.Certificate("/Users/alper.simsek/Bitirme/DeepFit-ML/database/ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
url = "/Users/alper.simsek/Bitirme/DeepFit-ML/data.tsv"

col_names_mfp = ["meal_id",	"user_id", "date",	"meal_sequence", "food_ids"]
dataset = pd.read_csv(url, sep='\t', na_values = "0.00", comment='\t', names=col_names_mfp, skipinitialspace=True, error_bad_lines=False,usecols=['food_ids', 'user_id'])
dataset = dataset.drop_duplicates(subset=["user_id"])
for index, food in dataset.iterrows():
    doc_ref2 = db.collection(u'users').document(str(food['user_id']))
    doc_ref2.set({
        u'id': food['user_id']
    })
    print(str(food['user_id']) + " written ")
