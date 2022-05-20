# Load CSV using Pandas
from pandas import read_csv
filename='pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)

url = 'https://goo.gl/bDdBiA'
datafrom = read_csv(url, names=names, verify=False)
print(datafrom.shape)