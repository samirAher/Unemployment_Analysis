import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Unemployment in India.csv")

print(df.head())

print(df.shape)

print(df.info())

df.columns = df.columns.str.strip()

print(df.columns)

print(df.isnull().sum())

print(df.describe())

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True
)

print(df.head())

plt.figure(figsize=(10,6))

sns.histplot(
    df["Estimated Unemployment Rate (%)"],
    kde=True
)

plt.title(
    "Distribution of Unemployment Rate"
)

plt.show()

plt.figure(figsize=(15,6))

sns.barplot(
    x="Region",
    y="Estimated Unemployment Rate (%)",
    data=df
)

plt.xticks(rotation=90)

plt.title(
    "State Wise Unemployment Rate"
)

plt.show()

plt.figure(figsize=(8,6))

sns.boxplot(
    x="Area",
    y="Estimated Unemployment Rate (%)",
    data=df
)

plt.title(
    "Urban vs Rural Unemployment"
)

plt.show()

top=df.groupby(
"Region"
)[
"Estimated Unemployment Rate (%)"
].mean()

top=top.sort_values(
ascending=False
)

top=top.head(10)

plt.figure(figsize=(12,6))

top.plot(
kind="bar",

)

plt.ylabel(
"Average Unemployment Rate (%)"
)

plt.xlabel(
"Region"
)

plt.title(
"Top 10 Regions by Unemployment"
)

plt.show()

numeric=df.select_dtypes(
include="number"
)

plt.figure(figsize=(8,6))

sns.heatmap(
numeric.corr(),
annot=True,
cmap="coolwarm"
)

plt.title(
"Correlation Heatmap"
)

plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY")

print(
"\nInsights:"
)

print(
"- Dataset analyzed successfully"
)

print(
"- Unemployment trends visualized"
)

print(
"- Regional comparison completed"
)

print(
"- Urban vs Rural analysis completed"
)

print(
"- Correlation analysis completed"
)