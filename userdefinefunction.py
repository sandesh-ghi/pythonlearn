#   function is a block of statement which can be used repetitively in a program.
#       pass data, known as parameters, into a function

# function is defined using the def keyword:




#creating function
def showdata():
    print("welcome to ktm")

#calling function
showdata()


#function arguments
# def sum(a,b):
    # print(a+b)
#calling with arguments
# sum(20,10)


#default parameter value

def sum(x,y=1):
    print(x+y)
sum(20)
sum(20,10)

#return values
def squre(x):
    return x*x,x*2
s=squre(5)
print(s)



