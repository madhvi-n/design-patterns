"""
The Strategy pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one as an object, and make them interchangeable. The pattern defines a common interface for all the algorithms, so that the client code can work with any of the algorithms without knowing their concrete classes.
"""

class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")


class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Debit Card")


class Wallet(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Wallet")


class ShoppingCart:
    def __init__(self):
        self.amount = 0
        self.payment_method = None

    def set_amount(self, amount):
        self.amount = amount

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def pay(self):
        self.payment_method.pay(self.amount)


def main():
    cart = ShoppingCart()
    cart.set_amount(100)

    # Set the payment method to Credit Card
    cart.set_payment_method(CreditCard())
    cart.pay()

    # Set the payment method to Debit Card
    cart.set_payment_method(DebitCard())
    cart.pay()

    # Set the payment method to Wallet
    cart.set_payment_method(Wallet())
    cart.pay()


"""
In this example, we have three concrete classes CreditCard, DebitCard and Wallet which are the strategies that we want to use. We also have a ShoppingCart class which is the client class that uses the strategy. We can see that the ShoppingCart class is not dependent on the concrete classes, it only cares about the interface(methods) of the classes. Now, if in future, we want to add more payment methods or change the way we pay, we can do it by just adding or changing the strategy class without affecting the client class.

This way the Strategy pattern can help us to encapsulate the algorithm and make them interchangeable, so that the client code can work with any of the algorithms without knowing their concrete classes. It allows a system to be independent of how its objects are created, composed and represented.
"""


if __name__ == '__main__':
    main()
