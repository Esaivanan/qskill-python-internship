import pandas as pd

data = pd.read_csv("data.csv")

print(data.head())
print(data.columns)

X = data[["bedrooms", "bathrooms", "sqft_living", "floors"]]
y = data["price"]

print("\nX (Features):\n", X.head())
print("\ny (Target):\n", y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nSample Predictions:\n", predictions[:5])

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nActual vs Predicted:\n", comparison.head())

print("\nAccuracy:", model.score(X_test, y_test))

import matplotlib.pyplot as plt

plt.scatter(y_test, predictions)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("House Price Prediction (Actual vs Predicted)")
plt.show()