import pandas as pd  
from sklearn.ensemble import RandomForestRegressor
import pickle 

print("Starting to train the model...")

#hkandan fail
df = pd.read_csv('housePrice.csv')

df['Area'] = df['Area'].astype(str).str.replace(',', '').str.strip()

df['Area'] = pd.to_numeric(df['Area'], errors='coerce')

#hazf maghadir hkali
df = df.dropna(subset=['Area', 'Room', 'Price'])
#vorodi va khorojii
X = df[['Area', 'Room']]
y = df['Price']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

with open('house_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("---ok---")

