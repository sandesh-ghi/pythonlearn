# Mutable data type : object change state or contents
# List
# Dictionary
# byte array

# Immutable data type : object cannot change
# int        a=5     5 is of type <class 'int'>
# Float     a=2.0    2.0 is of type <class 'float>
# Complex   a=1+2j   is of type <class 'complex'>
# String
# Tuple
# Set

a = 5
print(a, type(a))
a = 5.5
print(a, type(a))
a = 2 + 5j
print(a, type(a))

# string
s = 'Hello@123'
print(s, type(s))
s = '''
    Hello 
    welcome to ktm
'''
print(s)

s = '10'
print(s, type(s))

# list : order sequence of items.

l = [10, 'ws', 5.5]
print(l, type(l))

# tuple : same as a list order sequence it is defined within parenteses() wher item are seprated by comas.

t = (5, 'program', 1 + 3j)

print(t, type(t))
t = (10)
print(t, type(t))

# dictionary : is an unordered collection of key-value pairs.
# it defined within {} with each item being a pair in the form key:value

d = {
    'name': 'sandesh',
    'address': 'ktm 9'
}
print(d['name'])
print(d, type(d))

# Set : unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable(cannot be changed) {}

s= {10, 20, 30, 40}
print(s, type(s))
