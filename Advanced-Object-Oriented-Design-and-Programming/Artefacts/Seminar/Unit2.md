# Unit 2 Seminar : SOLID Principles of Object-Oriented Design

## Context
The Unit 2 seminar explored the five SOLID principles of object oriented design: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation and Dependency Inversion. The practical task was a hands-on refactoring session, where we took existing code and restructured it to follow these principles, to see how they improve maintainability and scalability in practice.

I refactored the shopping system so that Order only manages items and totals, and the payment logic lives in its own Payment abstraction with CreditCard and Paypal subclasses. Adding a new payment method is now just a new class, and checkout() depends on the abstraction, not a concrete payment. The full code is in the Individual Project section [Unit2-Case-Study](https://github.com/Elviix/E-portfolio/blob/main/Advanced-Object-Oriented-Design-and-Programming/Artefacts/Individual-project/Unit2-Case-Study.md). I only really understood the difference between the principles when I had to decide, line by line, which one my code was breaking, and this structure later became the foundation of my final artefact
