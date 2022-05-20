# View first 20 rows
from pandas import read_csv
filename="pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
peek = data.head(20)
print(peek)

# Dimensions of your data
shape = data.shape
print(shape)

# Data types for Each Attribute
types = data.dtypes
print(types)