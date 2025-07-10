from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(PaymentMethod):
    def pay(self,amount):
        print(f"Paid {amount} via UPI")
class manualpayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid {amount} via manualpayment")
upi = UPI()
upi.pay(100)
manual=manualpayment()
manual.pay(100)