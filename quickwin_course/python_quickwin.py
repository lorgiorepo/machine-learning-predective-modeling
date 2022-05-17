# Strings

data = 'Hello World'
print(data[0])
print(len(data))
print(data)

# Numbers
value = 123.1
print(value)
value = 10
print(value)

# Boolean
a = True
b = False
print(a, b)

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)

# No Value
a = None
print(a)

# If-Then-Else
value = 99
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe')


# For-Loop
for i in range(10):
    print(i)

# While-Loop
i = 0
while i < 10:
    print(i)
    i += 1

# Tuples: Readonly collections of items
a = (1, 2, 3)
print(a)

# List
mylist = [1, 2, 3]
print("Zeroth Value: %d" % mylist[0])
mylist.append(4)
print("List Length: %d" % len(mylist))
for value in mylist:
    print(value)


# Dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % mydict['a'])
mydict['a'] = 11
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys())
print("Values: %s" % mydict.values())
for key in mydict.keys():
    print(mydict[key])


# Functions
def mysum(x, y):
    return x + y

# Test sum function
result = mysum(1, 3)
print(result)