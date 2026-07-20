# Unit 10: Test-Driven Development and Unit Testing

## Context
Unit 10 covered Test-Driven Development, writing a failing test first, implementing just enough code to pass it, 
then refactoring, and the role of unit testing in code quality and maintainability. 
My practical work for this unit was the case study: designing, implementing and testing a secure e-learning platform using OO architecture and TDD.

## My work and reflection
I chose a layered architecture and implemented the User Management module test-first: for each feature I wrote a unittest describing what I wanted, 
watched it fail, then wrote just enough code to make it pass. The module hashes passwords with bcrypt, 
validates all input, and locks an account after three failed attempts. I ended up with thirteen tests covering registration, 
validation, authentication and lockout, and the one I cared about most checks that the classic injection string admin' OR '1'='1 cannot log anyone in. 
The full report and code are in the Individual Project section [Unit 10 Case study.pdf](https://github.com/Elviix/E-portfolio/blob/main/Advanced-Object-Oriented-Design-and-Programming/Artefacts/Individual-project/Unit10-Case-study.pdf)
. Working test-first felt slower at the start but changed how I code: the tests forced me to define the behaviour before writing it, and they gave me the safety net to refactor, 
moving magic numbers into constants and splitting validation into small helpers, without fear of breaking the login.
