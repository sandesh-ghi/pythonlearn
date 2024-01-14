#user input and type casting

#input
# a=eval(input("Enter The value1: "))
# b=int(input("Enter The value2: "))
# b=float(input("Enter The value2: "))
# b=eval(input("Enter The value2: "))
#type casting
# print(a+b)

#conditional statements
#if         if [condition expression]:
#           [statement(s) to execute]

#if else    if [condition expression ]:
#              [statement to execute]
#              else:
#                   [alternate statement to execute]

#if elif else       if[condition #1]:
#                       [statement #1]
#               elif[condition #2]
#                       [statement #2]
#               elif[condition #3]:
#                       [statement #3]
#               else:
#                       [statement when if and elif(s) are False]

# a=int(input("Enter the value: "))
# if a%2==0:
#     print(a,"even number")
# else:
#     print(a,"odd number")

subject1 = float(input("Enter number for dotnet: "))
subject2 = float(input("Enter number for E-MIS: "))
subject3 = float(input("Enter number for  CGA: "))
subject4 = float(input("Enter number for ITM: "))
subject5 = float(input("Enter number for Network: "))

# Calculate overall percentage
per = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
print("Percentage of Marks:",per)


# per=int(input("enter the value: "))
if per>=60:
    print("result:","first div")
elif per>=48:
    print("result:","second div")
elif per>=35:
    print("result:","third div")
else:
    print("result:","fail")





