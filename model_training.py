import pandas as pd  # For handling CSV data
from sklearn.linear_model import LinearRegression  # The ML model
import pickle  # To save the model

# Step 1: Load your dataset
df = pd.read_csv("house_data.csv")

# Step 2: Convert 'location' text values into numbers
df["location"] = df["location"].astype("category").cat.codes

# Step 3: Prepare the input features (X) and the target output (y)
X = df[["area", "bedrooms", "bathrooms", "location"]]  # Features
y = df["price"]  # What we want to predict

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Save the trained model into a file
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved successfully as model.pkl")
