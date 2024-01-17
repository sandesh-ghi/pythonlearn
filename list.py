#list->muitable->changable->declear [] ->coma seprated multiple value,
#create list-> l=[1,2,3,4,5]
#          index=[0,1,2,3,4]
#check list: print(type(l))

#print(l[2]) output: 3

#nested list
    #l=[1,2,3,[4,5,6])
    #           0,1,2
#index=[0,1,2,[  3  ]

#print(l[3][1])     output: 5

#Mixed list

#  -4 -3  -2      -1
#l=[2, 3, "hello",[3,4,5]]
#   0 1    2

#print(l[2]) output: hello


#list slicing
#print(l[0:2]   output: 2,3
#print(l[1:])   output: 3,"hello",[3,4,5]

#triple argument
#l=[1,2,3,4,5,6]
#print(l[0: :2])    output: 1,3,5
#reverse
#print(l[-1: :-1])  output: 6,5,4,3,2,1]

#  0  1   2  3   4
l=[10,30,40,50, "hello"]
#  -5 -4  -3 -4  -5
print(l[3],l[4])

print(l[0:2])       # : -> called 1 increment

print(l[0::2])      # :: -> called 2 increment

print(l[3:])

#reverse
print(l[-1::-1])    # : -> called -1 decrement
print(l[-1::-2])    # :: -> called -2 decrement


