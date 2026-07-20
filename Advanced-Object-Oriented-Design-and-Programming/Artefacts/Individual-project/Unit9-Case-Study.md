# Case Study (Unit 9) – Object-Oriented Software Architecture for an E-Commerce Platform

## Activity overview

- **Task:** As individuals, design an online shopping system for e-commerce company ShopEase, that can handle a large number of users, products, and transactions while ensuring scalability, maintainability, and security, using object-oriented software architecture.
- **Duration:** Unit 9.

## Requirements

1. **Scalability:** The system should handle a growing number of users and products.
2. **Modularity:** The system should be divided into independent modules (e.g., user management, product catalogue, order processing).
3. **Security:** The system must protect user data and transactions.
4. **Extensibility:** The system should allow for easy addition of new features (e.g., payment methods, recommendation engines).
5. **Object-Oriented Architecture Design:** The system will be designed using a layered architecture with the following layers:
   - Presentation Layer: Handles user interaction (e.g., web interface, mobile app).
   - Business Logic Layer: Implements core functionality (e.g., user authentication, product search, order processing).
   - Data Access Layer: Manages data storage and retrieval (e.g., databases, file systems). Each layer is further divided into modules, designed using object-oriented principles such as encapsulation, inheritance, and polymorphism.

## Guidance

1. Layered Architecture Overview (Unit 9 course material).
2. Modular Design with OOP: User Management Module, Product Catalog Module, Order Processing Module.
3. Security Practices: Authentication.
4. Scalability and Extensibility: Dependency Injection, Observer Pattern for Notifications.
5. Database Design (Data Access Layer).

## My code

```python
import bcrypt


class PasswordHasher:
    def hash(self, raw):
        return bcrypt.hashpw(raw.encode(), bcrypt.gensalt())

    def verify(self, raw, stored_hash):
        return bcrypt.checkpw(raw.encode(), stored_hash)

class User:
    def __init__(self, user_id, name, email, password_hash):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash

class UserRepository:
    def __init__(self):
        self.__users = {}

    def add(self, user):
        self.__users[user.user_id] = user

    def get(self, user_id):
        return self.__users.get(user_id)

class UserService:
    def __init__(self, repo, hasher):
        self.__repo = repo
        self.__hasher = hasher

    def register(self, user_id, name, email, raw_password):
        user = User(user_id, name, email, self.__hasher.hash(raw_password))
        self.__repo.add(user)

    def authenticate(self, user_id, raw_password):
        user = self.__repo.get(user_id)
        if user is None:
            return False
        return self.__hasher.verify(raw_password, user.password_hash)

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class ProductRepository:
    def __init__(self):
        self.__products = {}

    def add(self, product):
        self.__products[product.product_id] = product

    def get(self, product_id):
        return self.__products.get(product_id)

    def find_by_name(self, keyword):
        return [pro for pro in self.__products.values() if keyword.lower() in pro.name.lower()]

class ProductService:
    def __init__(self, repo):
        self.__repo = repo

    def add_product(self, product_id, name, price, stock):
        product = Product(product_id, name, price, stock)
        self.__repo.add(product)

    def search(self, keyword):
        return self.__repo.find_by_name(keyword)


# Usage
user_service = UserService(UserRepository(), PasswordHasher())
user_service.register("u1", "Vi", "vi@mail.com", "secret123")
print(user_service.authenticate("u1", "secret123"))   # True
print(user_service.authenticate("u1", "wrong"))       # False

product_service = ProductService(ProductRepository())
product_service.add_product("p1", "Laptop", 900, 5)
product_service.add_product("p2", "Phone", 500, 10)
print([p.name for p in product_service.search("lap")])  # ['Laptop']
```

The repositories handle storage and the services handle the logic, so the dict could be swapped for a real database without touching the services. I used bcrypt to hash passwords before storing them. The services get their repository and hasher through the constructor, which is dependency injection. The two modules are independent, so adding order processing later just means a new repository and service.
