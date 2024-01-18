#   python random randoint() Method
#   Return a number between 5 and 10 (both includeed)
#   import random
#   print(random.randint(5,10))

#   Return a number between 3(included) and 9 (not includeed)
#   print(random.randrange(3,9))

#   python Random choice() Method
#   return a random element from a list:
#   l=["apple","banana","cherry"]
#   print(random.choice(l))

#   RANDOM MODULE Function
#   random()    : Return a random float number between 0 and 1
#   Shuffle()   : Take a sequence and returns the sequence in a random order.
#   uniform()   : Return a random number between two given parameters.

import random
n = random.randint(5,10)
print(n)

n = random.randrange(3,9)
print(n)

l = ["apple","banana","cherry"]
n = random.choice(l)
print(n)

r=random.random()
print(r)

l=[10,20,30,40]
random.shuffle(l)
print(l)

u=random.uniform(3,9)
print(u)
