import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

cred = credentials.Certificate("/Users/alper.simsek/Bitirme/DeepFit-ML/database/ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
food_names = ["id","item"]

foodDS = pd.read_csv("/Users/alper.simsek/Bitirme/DeepFit-ML/items.tsv", sep='\t', na_values = "0.00", comment='\t', names=food_names, skipinitialspace=True, error_bad_lines=False)
spliter = lambda x: x.split('__')[-1:][0]
foodDS["item"] = foodDS["item"].apply(spliter).to_frame()
# doc_ref = db.collection(u'users').document(u'4')
# doc_ref.set({
#     u'userId': '4'
# })
finalDS = foodDS.drop_duplicates(subset=['item'])
for index, food in finalDS.iterrows():
    doc_ref2 = db.collection(u'food_ids').document(str(food['id']))
    doc_ref2.set({
        u'food_id': str(food['id']),
        u'name' : food['item']
    })
    print(str(food['id']) + " written " + food['item'])
