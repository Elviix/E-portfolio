# Collaborative Discussion 4 (Unit 8) – Refactoring Code Smells: Magic Numbers and Conditional Logic

## Activity overview

- **Discussion topic:** Analyse a pricing code snippet, identify code smells, and refactor to improve maintainability and readability.
- **Duration:** Unit 8 (this formative Collaborative Discussion starts and ends in this unit week).
- **Required posts:** Initial Post (≤300 words), peers reponses.

## Discussion Tasks

Identify at least two code smells in the provided code:

1. **Magic Numbers:**
   - Hardcoded discounts (0.9, 0.8) reduce readability and maintainability.
   - Problem: Changing discounts requires modifying the function directly.
2. **Long Method with Conditional Logic:**
   - The if-elif-else chain handles multiple discount rules in one place.
   - Problem: Adding new item types or discount rules bloats the function.
3. **Suggested Refactoring Techniques:**
   - Replace Magic Numbers with Constants: define discount factors as named constants (e.g., `BOOK_DISCOUNT = 0.9`).
   - Replace Conditional with Polymorphism (Strategy Pattern): encapsulate discount rules in separate classes (e.g., `BookDiscount`, `ElectronicsDiscount`).
4. **Refactored Code Structure:**
   - Option 1: Using Constants (simpler approach).
   - Option 2: Strategy Pattern (more scalable).

### Code Snippet

```python
def calculate_total_price(items):
    total = 0
    for item in items:
        if item['type'] == 'book':
            total += item['price'] * 0.9  # 10% discount for books
        elif item['type'] == 'electronics':
            total += item['price'] * 0.8  # 20% discount for electronics
        else:
            total += item['price']
    return total
```

## Initial Post

I identified two code smells.
The first is magic numbers. The values 0.9 and 0.8 are hard coded straight into the logic, so you only know what they mean from the comments, and changing a discount means editing the function itself. That hurts readability and makes mistakes easy.
The second is the long method with conditional logic. The if-elif-else chain stuffs every discount rule into one place, so each new item type adds another branch and the function keeps growing while doing two jobs at once: looping and pricing.
I went with the Strategy Pattern. Each discount becomes its own class and applies its own rule, with no type checking inside, so the conditional disappears entirely.

```python
class Item:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.discount.apply_discount(self.price)

def calculate_total_price(items):
    return sum(item.final_price() for item in items)

class BookDiscount:
    DISCOUNT = 0.9
    def apply_discount(self, price):
        return price * self.DISCOUNT


class ElectronicsDiscount:
    DISCOUNT = 0.8
    def apply_discount(self, price):
        return price * self.DISCOUNT

items = [Item(3, BookDiscount()), Item(10, ElectronicsDiscount())]
print(calculate_total_price(items))
print(ElectronicsDiscount().apply_discount(10))
```

Adding a discount just means writing one new class, with no edits to `calculate_total_price`.

## Peer Response 1

*In response to a peer's refactoring, which replaced the magic numbers and the if-elif chain with a dictionary lookup mapping item types to discount rates:*

Thanks for your clear analysis and I like that your refactor actually runs and returns the same total. The dictionary lookup is a neat way to kill both smells at once, since it removes the magic numbers and the if-elif chain in one step. One thing worth adding: the dictionary works well while each discount is a single fixed rate, but if the rules get more complex later, like bulk discounts or price thresholds, a flat lookup won't hold that logic and the Strategy Pattern you mentioned becomes the better fit. So your point about scaling is right, and the dictionary is a good middle ground for this size of example. Keeping the discount data separate from the calculation also means someone can change a rate without touching the loop, which is the main maintainability win here.

## Feedback Received from Peers

*Two peers reviewed my Strategy Pattern refactoring and responded:*

**Peer 1:** This is a clean implementation of the Strategy Pattern. I like that you pushed the discount logic all the way into the `Item` class itself, rather than keeping `calculate_total_price` responsible for any lookup. That's a nice separation, since the function now only does one job: summing final prices.

One thing worth discussing: your version requires the caller to explicitly attach a discount object at construction time, e.g. `Item(3, BookDiscount())`. That's different from the dictionary-lookup approach a few others used, where `calculate_total_price` still takes plain dictionaries with a 'type' string and looks up the matching strategy internally. Both approaches eliminate the conditional, but yours pushes the responsibility of "knowing which discount applies" onto whatever code creates the `Item`, while the lookup approach centralizes that decision in one place.
I could see your approach working nicely if items naturally arrive already knowing their category, say, pulled from a product database that also stores the discount type, so the mapping only happens once, upstream. But it also means every part of the codebase that constructs an `Item` needs to know which discount class to attach, which could get repetitive if items are created in several places.
Do you see this as mainly a tradeoff over who owns the type-to-discount mapping, or is there another advantage to keeping it on the `Item` itself I'm not weighing enough?

**Peer 2:** I enjoyed reading your post. Your explanation of the Strategy Pattern clearly shows how it removes the conditional logic and makes the code easier to extend. I also like how you included a working example to demonstrate how the refactored solution works.

## References (Harvard)

GeeksforGeeks (2026) *Strategy Design Pattern*. Available at: https://www.geeksforgeeks.org/system-design/strategy-pattern-set-1/ (Accessed: 24 June 2026).
