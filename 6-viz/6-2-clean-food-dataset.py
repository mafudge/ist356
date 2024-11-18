import pandas as pd
import numpy as np

def to_float(x):
    try:
        return float(x.strip())
    except:
        return np.nan

ff = pd.read_csv("./6-viz/data/fast_food_nutrition.csv")
ff.columns = ['company', 'item', 'calories','cal_from_fat','fat_g', 'sat_fat_g', 'trans_fat_g', 'cholesterol_mg', 'sodium_mg', 'carbs_g',  'fiber_g', 'sugars_g', 'protein_g', 'ww_points']
del ff['cal_from_fat']
del ff['ww_points']
for col in ff.columns:
    if col not in ['company', 'item']:
        ff[col] = ff[col].apply(to_float)

ff = ff.dropna()
print(ff.info())

ff.to_csv("./6-viz/data/fast_food_nutrition_cleaned.csv", index=False)

ff2 = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff2.info())
