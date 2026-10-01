# Think about a food delivery app like Swiggy/Zomato.
# Different payment methods exist:
# UPI
# - Credit Card
# - Cash on Delivery
# - Wallet

# Create the abstract class
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Any payment method in my application MUST provide a pay() method.


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via UPI")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via Credit Card")


class CashOnDeliveryPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via Cash on Delivery")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via Wallet")


payment = UPIPayment()
payment.pay(100)

payment = CreditCardPayment()
payment.pay(100)

payment = CashOnDeliveryPayment()
payment.pay(100)

payment = WalletPayment()
payment.pay(100)
