# Load CSV using numpy
from numpy import loadtxt
from urllib.request import urlopen
import ssl

filename='pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)

url = 'https://goo.gl/bDdBiA'
context = ssl._create_unverified_context()
rawdata = urlopen(url, context=context)
dataset = loadtxt(rawdata, delimiter=",")
print(dataset.shape)