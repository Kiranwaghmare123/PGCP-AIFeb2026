class Product:
    def __init__(self, price):
        self.__price = price
     
    @property 
    def price(self):
        return self.__price
        
p = Product(5000)
print(p.price)