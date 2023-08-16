import pandas as pd

data = pd.read_csv("data/dirty.csv")
print(data.to_string())
print()

# remove rows with empty cells
newdata = data.dropna()
print(newdata.to_string())
print()

# use original DataFrame to remove rows with empty cells
data.dropna(inplace=True)
print(data.to_string())
print()

df = pd.read_csv("data/dirty.csv")

# replace empty cells with 130
df.fillna(130, inplace=True)
print(df.to_string())
print()

# replace only specified columns
df = pd.read_csv("data/dirty.csv")
df["Calories"].fillna(130, inplace=True)
print(df.to_string())
print()

# replace using mean, median, or mode
df = pd.read_csv("data/dirty.csv")
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
print()

