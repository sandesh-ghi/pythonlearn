#   Queue is a linear data structure.
#   stores items in First In First Out (FIFO)

#   Enqueue: Add an items
#   dequeue: Remove an items
#   Front: Get the front item from queue
#   rear: Get the last item from queue.

l=[]
while True:
    c = int(input('''
    1 Enqueue element
    2 pop First elements
    3 Front elements
    4 Last Elements
    5 display element
    6 exit
    ''' "choose queue operation: "))
    if c==1:
        n=input("enter the value: ")
        l.append(n)
        print(" queue value: ",l)
    elif c==2:
        if len(l)==0:
            print(" queue element is empty")
        else:
            del l[0]
            # p=l.pop()
            # print(p)
            print("pop first element: ",l)
    elif c==3:
        if len(l)==0:
            print("queue element is empty: ")
        else:
            print("First queue value: ",l[0])
    elif c==4:
        if len(l)==0:
            print("element is empty: ")
        else:
            print("Last queue value: ",l[-1])
    elif c==5:
        print("display queue: ",l)
    elif c==6:
        break;
    else:
        print("invalid")