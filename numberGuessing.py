#   number guessing game Using Random Module
import random
Cnumber=random.randint(1,10)
userinput=int(input("Enter your guess number: "))
if userinput > Cnumber:
    print("Computer number",Cnumber)
    print("your guess number is too high")
elif Cnumber>userinput:
    print("Computer number",Cnumber)
    print("Your guess number is too low")
else:
    print("Computer number",Cnumber)
    print("Your guess number is equal")

