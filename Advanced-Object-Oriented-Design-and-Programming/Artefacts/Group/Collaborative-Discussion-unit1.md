# Collaborative Discussion 1 (Unit 4) – Structural Design Patterns: Adapter, Bridge and Composite

## Activity overview

- **Discussion topic:** Applying structural design patterns (Adapter, Bridge, Composite) to real-world scenarios, with Python code examples.
- **Duration:** Unit 4.
- **Required posts:** Initial Post (scenario, explanation and code example for each pattern), Peer Responses, 

## Discussion Tasks

1. **The Adapter Pattern** allows incompatible interfaces to work together. An adapter class acts as a bridge, translating requests/responses between the modern system and the legacy system.
   - Scenario: Integrating a legacy payment system (e.g., an old SOAP-based API) with a modern e-commerce platform (expecting RESTful JSON APIs).
   - Explain how the Adapter Pattern would solve the problem.
   - Share a code example (in Python) demonstrating the Adapter Pattern.
2. **The Bridge Pattern** separates abstraction from implementation and decouples abstraction (RemoteControl) from implementation (Device).
   - Scenario: Managing different devices (TV, Radio) and their remote controls (Basic, Advanced).
   - Explain how the Bridge Pattern would solve the problem.
   - Share a code example (in Python) demonstrating the Bridge Pattern.
3. **The Composite Pattern** allows you to compose objects into hierarchical structures (tree of objects). Both File and Folder implement the same interface (FileSystemComponent).
   - Scenario: Managing a file system where files and folders can be treated uniformly.
   - Explain how the Composite Pattern would solve the problem.
   - Share a code example (in Python) demonstrating the Composite Pattern.

## Initial Post

### Adapter Pattern

A legacy payment system like SOAP has compatibility issues with modern API. The Adapter Pattern fixes the issue by translating the legacy system to a modern one without changing the code.

```python
# legacy SOAP system
class LegacyPaymentSystem:
    def process_soap_payment(self, currency, amount):
        return f"Payment: {currency}{amount}"

# Modern e-commerce platform
class PaymentAdapter:
    def __init__(self):
        self.legacy = LegacyPaymentSystem()

    def pay(self, amount):
        return self.legacy.process_soap_payment("€", amount)

adapter = PaymentAdapter()
result = adapter.pay(60)
print(result)  # Payment: €60
```

### Bridge Pattern

The Bridge Pattern connects the abstraction (Remote) and the implementation (Device) via `self.device = device`. Both sides can grow independently without creating a new class for every combination.

```python
class Device:
    def turn_on(self): pass
    def turn_off(self): pass

class TV(Device):
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")

class Radio(Device):
    def turn_on(self):
        print("Radio ON")

    def turn_off(self):
        print("Radio OFF")

class Remote:
    def __init__(self, device):
        self.device = device
        self.is_on = False

    def togglepower(self):
        if self.is_on:
            self.device.turn_off()
            self.is_on = False
        else:
            self.device.turn_on()
            self.is_on = True


r1 = Remote(TV())
r1.togglepower()   # TV ON
r2 = Remote(Radio())
r2.togglepower()   # Radio ON
r2.togglepower()   # Radio OFF
```

### Composite Pattern

The Composite Pattern lets us treat files and folders the same way via a shared interface. In the code below, `FileSystem` is the common interface, `File` is the leaf and returns its own size, `Folder` is the composite: it loops through its children and delegates `get_size()` (recursively).

```python
class FileSystem:   # base component
    def get_size(self): pass

class File(FileSystem):  # Leaf (single object)
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def show(self):
        print(f"{self.name}, {self.get_size()} MB")

class Folder(FileSystem):  # Composite (contains other items)
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def get_size(self):
        total_size = 0
        for item in self.contents:
            total_size += item.get_size()
        return total_size

    def show(self):
        print(f"{self.name}, {self.get_size()} MB")
        for item in self.contents:
            item.show()

# usage
root = Folder("My Folder")                 # My Folder, 18 MB
documents = Folder("My Documents")         # My Documents, 18 MB
documents.add(File("resume.pdf", 12))      # resume.pdf, 12 MB
documents.add(File("cover_letter.pdf", 6)) # cover_letter.pdf, 6 MB

root.add(documents)
root.show()
print(f"Size: {root.get_size()} MB")  # Size: 18 MB
```

## Peer Response 1


I have reviewed your Bridge Pattern code and noted a few architectural vulnerabilities that would hold it back in a production environment. Examples:
•Your Device class uses pass for its methods. In Python, this doesn't actually force subclasses like TV or Radio to implement turn_on or turn_off. If a developer creates a Speaker(Device) class but forgets to define turn_on(), Python won't complain until runtime when the code crashes.
•The Remote tracks whether the device is on via self.is_on. This is dangerous. The Device should be the single source of truth for its own state. If someone turns the TV on manually (via a physical button or a different remote object), your Remote state becomes completely desynchronized from reality.
•Because Python is dynamically typed, a developer could technically pass anything into Remote(device). Explicitly type-hinting the Device abstract class ensures better IDE auto-complete and static analysis linting.
To fix these issues, use Python’s built-in abc module to enforce the interface, and delegate the power state entirely to the implementation side.

