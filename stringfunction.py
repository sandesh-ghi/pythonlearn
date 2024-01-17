#python string function
#lower()
#upper()
#title()
#capitalize()

# w=("If you're looking for random paragraphs, you've come to the right place.")
# n=w.lower();
# print(n,"\n")
# print(n.upper(),"\n")
# print(n.capitalize(),"\n")
# print(n.title(),"\n")

# u=w.upper()
# print(u,"\n")
#
# t=w.title()
# print(t,"\n")
#
# r=w.capitalize()
# print(r)


#python function...
#find() -> return index number
#index()
#isalpha() -> true or false only alphabate
#isdigit() -> all digite
#isalnum() -> number or character value

w="welcome"
# print(w.find('z',2))
#print(w.index('e'))

print(w.isalpha())
w="123"
print(w.isdigit())

w="welcome@123"
print(w.isalnum())

#conver integer 65 to ASCII Character('A')
a=100
print(chr(a))

#conver ASCII unicode Character 'A' to 65
y='H'
print(ord(y))

#string format() Method ->

w="welcome {} to {} Ktm".format("hello" ,10);
print(w)

w="welcome {1} to {0} Ktm".format("hello",10);
print(w)

w="welcome {a:10} to {b} ktm".format(a=30,b=40); # space change: center{a:^10} , left {a:<10}, right  {a:>10}
print(w)
