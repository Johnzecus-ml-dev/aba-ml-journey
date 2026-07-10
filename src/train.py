import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

# 1. Create dummy training data - REPLACE THIS WITH YOUR REAL DATA
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  # features
y = np.array([10, 20, 30, 40, 50])  # target

# 2. Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train the model
model = LinearRegression()
model.fit(X_scaled, y)

# 4. Make sure models folder exists
os.makedirs("models", exist_ok=True)

# 5. Save them
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Training done! model.pkl and scaler.pkl saved in models/")
