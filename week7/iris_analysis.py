# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
try:
    iris_raw = load_iris()
    iris_df = pd.DataFrame(data=iris_raw.data, columns=iris_raw.feature_names)
    iris_df['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Check data types and missing values
print("\nData types:")
print(iris_df.dtypes)

print("\nMissing values:")
print(iris_df.isnull().sum())

# Clean dataset (no missing values in Iris, but here's how you'd handle it)
iris_df.dropna(inplace=True)

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(iris_df.describe())

# Group by species and compute mean of numerical columns
grouped = iris_df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped)

# Observations
print("\nObservations:")
print("Setosa has the smallest petal measurements, while Virginica has the largest.")
print("Sepal length and petal length seem to increase together across species.")

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line chart: simulate time-series by plotting index vs sepal length
plt.figure(figsize=(8, 4))
plt.plot(iris_df.index, iris_df['sepal length (cm)'], label='Sepal Length')
plt.title("Sepal Length Over Sample Index")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart: average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=iris_df)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram: distribution of sepal width
plt.figure(figsize=(6, 4))
plt.hist(iris_df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter plot: sepal length vs petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()