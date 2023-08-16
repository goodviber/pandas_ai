import pandas as pd

# format dates
df = pd.read_csv('data/dirty.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
print()

# remove rows with null values in the "Date" column
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())
print()

# set duration to 45 min in row 7
df.loc[7, 'Duration'] = 45
print(df.to_string())
print()

# set duration to 45 mins where duration is 60
df.loc[df['Duration'] == 60, 'Duration'] = 45
print(df.to_string())
print()

df = pd.read_csv('data/dirty.csv')

# delete rows where duration is greater than 45 min
df.drop(df[df['Duration'] > 45].index, inplace=True)
print(df.to_string())
print()
