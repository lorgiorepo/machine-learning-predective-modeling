# Basic Line Plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# Basic scatter plot
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x, y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()