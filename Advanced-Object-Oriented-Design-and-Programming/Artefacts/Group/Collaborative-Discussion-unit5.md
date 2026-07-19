# Collaborative Discussion 2 (Unit 5) – Refactoring with the Strategy Pattern

## Activity overview

- **Discussion topic:** Analyse a payment-processing code snippet and refactor it using the Strategy Pattern.
- **Duration:** Unit 5 (this formative Collaborative Discussion starts and ends in this unit week).
- **Required posts:** Initial Post (≤300 words).

## Discussion Tasks

1. Identify the problems in the current implementation.
2. Explain how the Strategy Pattern can improve the code.
3. Provide a refactored version of the code using the Strategy Pattern.
4. Discuss the benefits of using the Strategy Pattern in this scenario.

### Code Snippet

```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount}")
        elif payment_type == "bank_transfer":
            print(f"Processing bank transfer of ${amount}")
        else:
            raise ValueError("Invalid payment type")
```

### Guidance

- **Problems in the Current Implementation:**
  - Violates Open/Closed Principle (OCP): Adding a new payment method (e.g., Crypto) requires modifying the PaymentProcessor class.
  - Tight Coupling: The process_payment method directly handles all payment logic, making it hard to maintain.
  - Poor Readability: Long if-elif chains become unwieldy as payment methods grow.
- **How the Strategy Pattern Solves These Issues:**
  - Encapsulates Algorithms: Each payment method becomes a separate strategy class (e.g., CreditCardPayment, PayPalPayment).
  - Decouples Logic: The PaymentProcessor delegates payment processing to interchangeable strategies.
  - Extensible: New payment methods can be added without modifying existing code.
- **Refactored Code Structure (Using Strategy Pattern):**
  - Step 1: Define the Strategy Interface.
  - Step 2: Implement Concrete Strategies.
  - Step 3: Refactor PaymentProcessor.
  - Step 4: Usage Example.

## Initial Post

The original PaymentProcessor relies on a long if–elif chain keyed on a string payment_type. This breaks the Open/Closed Principle. Indeed, adding a method like Crypto means editing the class itself, risking existing logic. It's tightly coupled, since all payment behaviour lives in one method, and readability degrades as methods grow. Strings are easy to get wrong, and the mistake stays hidden until the code runs.

I improved the code by using the Strategy Pattern, which encapsulates each payment method as its own class behind a shared interface. The processing logic is decoupled from the client, and methods become interchangeable. New payment types can be added simply by writing a new class, with no changes to existing code.

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): ...


class CreditCard(PaymentStrategy):
    def pay(self, amount): print(f"Credit card {amount}")

class Paypal(PaymentStrategy):
    def pay(self, amount): print(f"Paypal {amount}")

class BankTransfer(PaymentStrategy):
    def pay(self, amount): print(f"Bank transfer {amount}")

class Checkout:
    def __init__(self, strategy): self.strategy = strategy
    def complete(self, amount): self.strategy.pay(amount)

Checkout(CreditCard()).complete(20)
Checkout(BankTransfer()).complete(100)
```

I used abstractmethod to enforce the interface so every strategy must implement pay. Checkout acts as the context, delegating to whichever strategy it's given. This code is extensible: we can add new methods without touching Checkout. It's easier to test, since each strategy is isolated.

## Peer Response 1

*In response to a peer's Strategy Pattern refactoring, which framed OCP as "modification vs extension" and included a set_strategy method for switching payment type at runtime:*

Thank you for you post . The modification vs extension framing makes OCP click straight away, and "strike two" for SRP is a great line. The set strategy method is great as well, swapping payment type at runtime without rebuilding anything is the pattern really earning its keep.

