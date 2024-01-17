#del
#pop()
#remove()
#clear()


# l=[20,30,50,60]

# del l[1]
# l.pop(2)
# print(l.pop(2))
# l.remove(60)
# l.clear()
# print(l)

# update element from list
#insert()
#append()-> data  append list [20,30,40]-> l.append(60) [20,30,40,60]
#extends()   :[20, 30, 50, 60, 50, 60]

# l=[20,30,50,60]
# l[0]=10
# l.insert(0,10)
# l.append(10)
# n=[50,60]
# l.append(n)
# l.extend(n)
# print(l)



#count()
#max()
#min()
#sort()
#reverse()
#index()

# l = [10,20,30,10,10,50,5,15,25]
# a = ["hello","world"]
# c = l.count(10)

# m = max(l)
# m=max(a)
# m=min(a)
# print(m)

# l.sort()
# l.reverse()
# b=l.index(25)
# print(b)


# zip

# l=[10,20,40,50]
# l1=[3,4,77,88]

# t=len(l)

# for a,b in zip(l,l1):         #l1=[3,4,77,88,90]
#     print(a,b)

# for j in range(t):
#     print(l[j],l1[j])


#string list

# n=input("Enter a string value: ")
#
# print(n)
#
# l=n.split();
# print(l)


l=[]
for a in range(1,4):
    n=input("Enter a string value"+str(a)+": ")
    print(n)
    l.append(n)
print(l)


