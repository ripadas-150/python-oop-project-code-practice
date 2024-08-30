class phone :
    Brand : "Samsung"
     
    def __init__(self,num,brand,price ):
        self.num = num
        self.brand = brand
        self.price = price
        
    
    def F(self):
        print(self.num,self.brand,self.price)
my_phone = phone(1713861,"samsung",5800)
my_phone.F()
