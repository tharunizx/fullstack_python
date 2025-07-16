class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def getPrice(self):
        print(self.price)
p1=Product("Laptop",50000)
p2=Product("Mouse",500)
print(f"First product {p1.name}, price is {p1.getPrice}rs.")
print(f"Second product {p2.name}, price is {p2.price}rs.")