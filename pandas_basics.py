import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print("Pandas Version: ", pd.__version__)
print("\nCar Passing DataFrame")
print(myvar)


### One dimensional series
a = [1, 7, 2]

myvar = pd.Series(a)

print("\nOne Dimensional Pandas Series")
print(myvar)
#print(myvar[1])


### One dimensional with labels

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])

print("\nOne Dimensional Pandas Series with Labels")
print(myvar)
# print(myvar["y"])


### Pandas series from input dictionary

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

print("\nCalories Series")
print(myvar)


## DataFrames from 2 series

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print("\nPandas DataFrame with 2 series")
print(myvar)