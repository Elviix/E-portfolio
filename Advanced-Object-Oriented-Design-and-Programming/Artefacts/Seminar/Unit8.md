# Unit 8: Refactoring and Code Smells

## Context
Unit 8 covered code smells, indicators of poor design like long methods, duplicate code and magic numbers, and the refactoring techniques that remove them, 
such as Extract Method and Replace Conditional with Polymorphism. 
My practical work for this unit was Collaborative Discussion 4, where we analysed a pricing function containing several smells and refactored it.

## My work and reflection
In my initial post I identified two smells in the provided code: magic numbers, since the discounts 0.9 and 0.8 were hard coded into the logic, 
and a long method with conditional logic, where the if elif else chain kept growing with every new item type. 
I refactored it with the Strategy Pattern, so each discount became its own class and the conditional disappeared entirely: adding a discount now just means writing one new class, 
with no edits to calculate_total_price. My full post, code and the exchanges with my peers are in the Collaborative Discussion section [Collaborative-Discussion4-unit8](https://github.com/Elviix/E-portfolio/blob/main/Advanced-Object-Oriented-Design-and-Programming/Artefacts/Group/Collaborative-Discussion4-unit8.md). This exercise connected directly to my final artefact, 
because Replace Conditional with Polymorphism is exactly what my Transaction hierarchy does with Deposit and Withdraw.
