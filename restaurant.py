# class restaurantTable:
#     menus = {
#         'pizza' :5000,
#         'cola' : 600,
#         'apple juice' : 2000,
#         'hambuger' : 1000,
#         'fried potato' : 1500
#     }

#     def __init__(self):
#         self.total = 0
#         self.orders = []

#     def addOrder(self,order):
#         self.total += self.menus[order]
#         self.orders.append(order)

#     def printBill(self):
#         for order in self.orders:
#             print(f'{order} : {self.menus[order]}.')
#         print(f'Total price is {self.total}.')    

# def startProgram():
#     table = restaurantTable()

#     while True:
#         order = input("Order: ")
#         table.addOrder(order)     

#         another = input("Order again: y/n: ") 
#         if another == 'y':
#             continue
#         if another == 'n':
#             table.printBill()   
#             break


class restaurantTable:
    menus = {
        'pizza' :5000,
        'cola' : 600,
        'apple juice' : 2000,
        'hambuger' : 1000,
        'fried potato' : 1500
    }

    def __init__(self):
        self.total = 0
        self.orders = []

    def addOrder(self,order):
        self.total += self.menus[order]
        self.orders.append(order)

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}.')
        print(f'Total price is {self.total}.')    

def startProgram():
    table = restaurantTable()

    while True:
        order = input("Order: ")
        table.addOrder(order)     

        another = input("Order again: y/n: ") 
        if another == 'y':
            continue;
        if another == 'n':
            table.printBill()   
            break;          