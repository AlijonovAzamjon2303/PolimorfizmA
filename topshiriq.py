import uuid

class Product:
    def __init__(self, name, price, quantity):
        self.__id = uuid.uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} - {self.price} x {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor xolos")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f" {self.warranty}"
        return data


class Basket:
    def __init__(self):
        self.__id = uuid.uuid4()
        self.__data = []

    def add(self, product):
        pass

    def remove(self, product_name):
        pass


# 1. id bo'lsin
# 2. Menyular orqqali basket funksiyalarini ishlatib kelish
# 3. Basket ichidagi methodlarni ishlashida priductning id attributini ishlatish