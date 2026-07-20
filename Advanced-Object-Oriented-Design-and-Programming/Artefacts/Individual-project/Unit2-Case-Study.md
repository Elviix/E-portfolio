# Case Study (Unit 2) – Designing a Real-World Application with SOLID Principles

## Activity overview

- **Task:** As individuals, design a simple online shopping system that allows users to add products to a cart, calculate the total price, and apply discounts. Start with a poorly designed code in Python, then refactor it to adhere to the SOLID principles.
- **Duration:** Unit 2.

## Problems with the Initial Code

1. The Order class handles cart management, total calculation, and payment processing (SRP violation).
2. Adding a new payment method requires modifying the Order class (OCP violation).
3. Tight coupling between Order and payment methods (DIP violation).

### Initial Code

```python
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def pay(self, payment_type):
        if payment_type == "credit":
            print("Processing credit card payment...")
        elif payment_type == "paypal":
            print("Processing PayPal payment...")  # Adding a new method requires modifying this class.
```

## Refactored Code Steps (SOLID Principles)

1. **Single Responsibility Principle (SRP):**
   - Problem: Order does too much.
   - Solution: Split into Order (manages items and calculates totals) and PaymentProcessor (handles payments).
   - Improvement: Order no longer handles payments.
2. **Open/Closed Principle (OCP):**
   - Problem: Adding a new payment method requires modifying PaymentProcessor.
   - Solution: Use abstraction (e.g., an interface or abstract class).
3. **Liskov Substitution Principle (LSP):**
   - Problem: Subclasses should replace their parent class without breaking functionality.
   - Solution: Ensure all PaymentMethod subclasses implement pay() correctly.
   - Improvement: CryptoPayment can replace PaymentMethod without issues.
4. **Interface Segregation Principle (ISP):**
   - Problem: If PaymentMethod had unrelated methods, subclasses would be forced to implement them.
   - Solution: Keep interfaces small and focused.
   - Improvement: Classes only implement what they need.
5. **Dependency Inversion Principle (DIP):**
   - Problem: High-level Order depends on low-level PaymentProcessor.
   - Solution: Depend on abstractions (PaymentMethod).
   - Improvement: Order depends on PaymentMethod (abstraction), not concrete classes.

## My Code

```python
from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.items = []     # start with an empty list

    def add_item(self, items, price):
        self.items.append({"name": items, "price": price})  # use a dictionary, code reads clearly
        return self.items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def checkout(self, payment):
        total = self.calculate_total()
        print(f"Total to pay: {total}£")
        payment.payment_method()

class Payment(ABC):
    @abstractmethod
    def payment_method(self):
        pass

class CreditCard(Payment):
    def payment_method(self):
        print("Processing credit card payment ...")

class Paypal(Payment):
    def payment_method(self):
        print("Processing paypal payment ...")


o1 = Order()
o2 = Order()
print(o1.add_item("T shirt", 20))
print(o2.add_item("Jean", 25))
o1.checkout(Paypal())
o2.checkout(CreditCard())
```

Order only manages items and totals now, the payment logic lives in its own classes (SRP). 
Adding a new payment method just means writing a new Payment subclass, no edits to Order (OCP). 
Any subclass can be passed to checkout() and works the same way (LSP). The Payment interface has a single method, so subclasses only implement what they need (ISP). 
And checkout() depends on the abstraction, not on a concrete payment class (DIP).
