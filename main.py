from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

dataset_path = "data.tsv"

#col_names_awram = ["ndb_no","shrt_desc","water_g","energ_kcal","protein_g","lipid_tot_g",
#                   "ash_g","carbohydrt_g","fiber_td_g","sugar_tot_g","calcium_mg",
#                   "iron_mg","magnesium_mg","phosphorus_mg","potassium_mg","sodium_mg","zinc_mg","copper_mg",
#                   "manganese_mg","selenium_ug","vit_c_mg","thiamin_mg","riboflavin_mg","niacin_mg",
#                   "panto_acid_mg","vit_b6_mg","folate_tot_ug","folic_acid_ug","food_folate_ug","folate_dfe_ug",
#                   "choline_tot_mg","vit_b12_ug","vit_a_iu","vit_a_rae","retinol_ug","alpha_carot_ug","beta_carot_ug","beta_crypt_ug",
#                   "lycopene_ug","lut_zea_ug","vit_e_mg","vit_d_ug","vit_d_iu","vit_k_ug","fa_sat_g","fa_mono_g","fa_poly_g","cholestrl_mg","gmwt_1",
#                   "gmwt_desc1","gmwt_2","gmwt_desc2","refuse_pct"]

col_names_mfp = ["meal_id",	"user_id", "date",	"meal_sequence", "food_ids"]

raw_dataset = pd.read_csv(dataset_path, sep='\t', na_values = "0.00", comment='\t', names=col_names_mfp, skipinitialspace=True, error_bad_lines=False,
    usecols=['food_ids', 'user_id'])

dataset = raw_dataset.copy()
print(dataset) 
print(dataset.shape)
print(dataset.isna().sum())

