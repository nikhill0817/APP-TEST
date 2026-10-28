import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print("First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

print("\nStudents Scoring Above 75:")
print(df[df["Marks"] > 75])

# Bar Chart
df.plot(x="Name", y="Marks", kind="bar")
plt.title("Student Marks")
plt.show()

# Histogram
df["Marks"].plot(kind="hist")
plt.title("Distribution of Marks")
plt.show()

# Scatter Plot
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()