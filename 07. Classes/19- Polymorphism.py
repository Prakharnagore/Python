class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class Wallet:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


upi = UPI()
card = CreditCard()
wallet = Wallet()

# All three objects have the same method: pay()
# But they behave differently.

upi.pay(500)  # Paid ₹500 using UPI
card.pay(500)  # Paid ₹500 using Credit Card
wallet.pay(500)  # Paid ₹500 using Wallet

# This is called polymorphism.
