#List comprehesion is  an elegat way to define and create lists based on exiting lists.
#List compreshension is generally more compact and faster than normal functions and loops for creating list

#syntax of list comprehension
# [expression for item in list]

l=[]
for a in range(1,101):
    # print(a)
    l.append(a)
print(l)


n=[m for m in range(1,101) if m%2==0]
print(n)

s="hello world"
d=[g for g in s]
print(d)