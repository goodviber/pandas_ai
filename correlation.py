import pandas as pd

# show correlation between columns

df = pd.read_csv("data/correlation.csv")
print(df.corr())
print()