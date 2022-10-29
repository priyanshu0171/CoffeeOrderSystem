import os
class Coffee:
    def __init__(self):
        self.PRODUCTS ={} 
        self.set_products()
        
    def set_products(self):
        # Product Setter Function
        self.PRODUCTS = {
            "Espresso": [60, 75, 100],
            "Cappuccino": [80, 90, 125],
            "Latte": [100, 125, 150]
        }
    def get_products(self):
        # Product Getter Function
        print("\nALL AVAILABLE PRODUCTS:\n")
        print("{:<15} {:<8} {:<8} {:<8}".format(
            'Product/Add on', 'Milk', 'Cream', 'Latte'))
        for i in self.PRODUCTS.keys():
            print("{:<15} {:<8} {:<8} {:<8}".format(
                i, self.PRODUCTS[i][0], self.PRODUCTS[i][1], self.PRODUCTS[i][2]))
    

class Orders(Coffee):
    def __init__(self):
        super().__init__() 
        self.grandTotal = 0   
        self.addedProducts = []  #format => [{coffee: espresso, addon: milk, amount: 60 }]
        
    def calculateBillAmount(self, coffee, addon):
        addonMAP = {0:"Milk", 1:"Cream", 2:"Latte"} # local Map of Addons
        for i,j in enumerate(self.PRODUCTS.keys()):
            if i+1 == coffee:
                self.addedProducts.append({"coffee": j,"addon":addonMAP[addon-1],"amount":self.PRODUCTS[j][addon-1]})
                return self.PRODUCTS[j][addon-1]
        return 0


    def start(self):
        # display All the possible Combinations of Products
        self.get_products() 
        print("\nENTER THE NUMBER OF COFFEE TO ORDER->")
        for i,j in enumerate(self.PRODUCTS.keys(), start=1):
            print("{:<8} {:<8}".format(i,j))
        coffee = int(input("\nEnter Your Choice: "))
        print("\nWHAT WOULD YOU LIKE TO ADD->->")
        print("{:<8} {:<8}".format(1,'Milk'))
        print("{:<8} {:<8}".format(2,'Cream'))
        print("{:<8} {:<8}".format(3,'Latte'))
        addon = int(input("\nEnter Your Choice: "))
        if coffee == 1:
            amount = self.calculateBillAmount(1, addon)
        elif coffee == 2:
            amount = self.calculateBillAmount(2, addon)
        elif coffee == 3:
            amount = self.calculateBillAmount(3, addon)
        if amount == 0:
            print("There was an error completing your request")
            return False
        else:
            self.grandTotal+=amount
            print("\nDo you wish to add more?\n1\tYES\n2\tNO")
            choice = int(input("Enter your Choice: "))
            if choice == 1:
                return True
            elif choice == 2:
                self.GenerateBill()
                return False

    def GenerateBill(self):
        # Uncomment on MAC or LINUX
        # os.system('clear')  
        os.system('cls')
        print("\nBill for your order is\n")
        print(f"TOTAL NUMBER OF ITEMS: {len(self.addedProducts)}\n")
        print("{:<10} {:<10} {:<10}".format("Coffee", "Add On", "Amount"))
        for product in self.addedProducts:
            print("{:<10} {:<10} {:<10}".format(product["coffee"], product["addon"], product["amount"]))
        print("{:<10} {:<10} {:<10}".format("Total"," ", self.grandTotal))


newOrder = Orders()
while True:
    os.system('cls')
    # Uncomment on MAC or LINUX
    # os.system('clear')    
    if newOrder.start():
        pass
    else:
        newOrder.GenerateBill()
        break