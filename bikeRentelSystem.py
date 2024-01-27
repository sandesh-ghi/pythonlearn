


class bikeShop:
    def __init__(self , stock):
        self.stock = stock
    def displayBike(self):
        print("Total Bikes: ",self.stock)
    def rentForBike(self,q):            # q-> number of quentity


        if q<=0:
            print("Enter the +ve or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock) ")

        else:
            print("Total Prince:", q*100)
            print("Total Bikes:",self.stock-q)


while True:
    obj = bikeShop(100)
    uc=int(input('''
    1.Display Stocks
    2.Rent a Bike
    3.Exit
    Enter your operation:  '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the QTY: "))
        obj.rentForBike(n)
    else:
        break




