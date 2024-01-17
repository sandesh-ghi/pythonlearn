#linear data structure
# store items in a Last-in/First-out(LIFO) or First-in /Last-out(FILO)

#   Push => indexing an elements
#   pop => Deleting an element(last element)
#   peek => Display the last element
#   Display => display list

l=[]
while True:
    c = int(input('''
    1 push element
    2 pop elements
    3 peek elements
    4 display element
    5 exit
    ''' "choose stack operation: "))
    if c==1:
        n=input("enter the value: ")
        l.append(n)
        print("append stack value: ",l)
    elif c==2:
        if len(l)==0:
            print("element is empty")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("element is empty: ")
        else:
            print("last stack value: ",l[-1])
    elif c==4:
        print("display stack: ",l)
    elif c==5:
        break;
    else:
        print("invalid")



