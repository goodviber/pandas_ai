import pandas as pd


mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print()
print("version", pd.__version__)
print()

# Series is a one-dimensional array

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print("First value of series is", myvar[0])
print()

# Create your own index
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print("Value of y is", myvar["y"])
print()

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print()

myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
print()

# DataFrames is a two-dimensional array

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)
print()

# refer to the row index
print(myvar.loc[0])
print()

# use a list of indexes
print(myvar.loc[[0, 1]])
print()

# use named indexes
myvar = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(myvar)
print()

# refer to the named index
print(myvar.loc["day2"])
print()

# load files into a DataFrame
myvar = pd.read_csv("data/data.csv")
print(myvar.to_string())
print()

# print the first 5 rows of the DataFrame
print(myvar.head())
print()

# print the last 5 rows of the DataFrame
print(myvar.tail())
print()

# print number of maximum rows
print("Max Rows", pd.get_option("display.max_rows"))
print()

# print information about the data
print(myvar.info())
print()

# print a statistical summary of the data
print(myvar.describe())
print()

# with JSON files
myvar = pd.read_json("data.json")
print(myvar.to_string())
print()
print(myvar)
