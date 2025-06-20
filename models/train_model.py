
import pandas as pd
from xgboost import XGBRegressor
import pickle

data = pd.read_csv("../data/cleaned_soil_data.csv")
X = data[['rainfall']]
y = data['carbon_stock']

model = XGBRegressor()
model.fit(X, y)

# Save model
with open("../models/sequestration_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model trained + saved.")
