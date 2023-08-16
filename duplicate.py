import pandas as pd

# print duplicate rows
df = pd.read_csv("data/duplicate.csv")
print(df.duplicated())
print()

# remove duplicate rows
df.drop_duplicates(inplace=True)
print(df.to_string())
print()
