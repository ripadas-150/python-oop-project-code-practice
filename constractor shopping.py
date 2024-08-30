class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self,item,price,quantity):
        product = {"item" : item,"price" : price,"quantity" : quantity} 
        self.cart.append(product)
    
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item["price"] * item["quantity"]
        print("total price", total )
        if amount < total :
            print(f"please provide {total-amount} more")
        else :
            extra = amount - total
            print(f"Here is your extra money {extra}")
            
    def remove_item(self,item):
        pass

    
ripa = shopping("Ripa")
ripa.add_to_cart("alu",50,6)
print(ripa.cart)

ripa.checkout(600)
