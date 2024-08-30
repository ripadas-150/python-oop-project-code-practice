class calculator :
    Brand : "Casio 1999"
     
    def add(self,num1,num2 ):
        self.add = num1+num2
        return self.add
    
    def sub(self,num1,num2 ):
        self.sub = num1-num2
        return self.sub
    
    def mul(self,num1,num2 ):
        self.mul = num1*num2
        return self.mul
    
    
count = calculator()
print(count.add(10,20))
print(count.sub(10,20))
print(count.mul(10,20))
         

