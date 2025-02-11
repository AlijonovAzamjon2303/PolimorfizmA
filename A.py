class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} - {self.quantity} x {self.price}"

    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Mahsulot yetarli emas!")

    def restock(self, amount):
        self.quantity += amount

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        return f"{self.name} - {self.quantity} x {self.price} | {self.warranty}"

e = Electronics("A", 12, 100, "1 yil")
print(e.info())