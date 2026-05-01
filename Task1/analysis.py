import pandas as pd
data = pd.read_csv("supermarket_sales.csv")
print(data.head())

print(data.info())
print(data.describe())

print("Average Final Grade (G3):", data["G3"].mean())
print("Average Study Time:", data["studytime"].mean())
print("Average Absences:", data["absences"].mean())

import matplotlib.pyplot as plt

data["G3"].value_counts().sort_index().plot(kind="bar")
plt.title("Final Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

plt.scatter(data["studytime"], data["G3"])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("G3")
plt.show()

import seaborn as sns

plt.figure(figsize=(10,6))
sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()