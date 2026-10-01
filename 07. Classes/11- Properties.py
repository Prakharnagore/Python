class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
# Old way to do this is to use get_price and set_price directly
print(product.get_price())
print(product.set_price(10))

# Now better way to do this is to use properties, but the two get_price and set_price methods are still visible
print(product.price)  # 10
product.price = -1  # ValueError: Price cannot be negative
product.price = 20  # 20

# Now more better way to do this is to use properties decorator


class ProductProperties:
    def __init__(self, price):
        self.__price = price

    # @classmethod - make the instance method a class method
    # @staticmethod - make the instance method a static method

    @property  # make the instance method a getter method
    def price(self):
        return self.__price

    @price.setter  # make the instance method a setter method
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = ProductProperties(-10)
print(product.price)  # ValueError: Price cannot be negative
product.price = -1  # ValueError: Price cannot be negative
product.price = 20  # 20
