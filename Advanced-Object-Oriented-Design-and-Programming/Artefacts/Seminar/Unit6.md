# Unit 6 Seminar: Concurrency and Parallelism in Object-Oriented Design

## Context
The Unit 6 seminar covered concurrency and parallelism: the difference between threads and processes, 
synchronisation mechanisms like locks and semaphores, and the classic concurrency problems, race conditions and deadlocks. 
The practical exercise was to write a thread-safe bank account in Python with concurrent deposits and withdrawals.



import threading

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        self._lock = threading.Lock()

    def deposit(self, amount):
        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        with self._lock:
            if amount <= self._balance:
                self._balance -= amount
                return True
            return False

    def get_balance(self):
        with self._lock:
            return self._balance

account = BankAccount(100)

def make_deposits():
    for _ in range(1000):
        account.deposit(1)
threads = [threading.Thread(target=make_deposits) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

The balance is protected by a threading.Lock, so only one thread can change it at a time, and even reading goes through the lock. Ten threads making a thousand deposits each always give exactly 10100, never less, which proves there is no race condition. I then built on this small class for the graded Unit 6 exercise, adding validation with penalties, transfers with ordered locking to prevent deadlock, the Command pattern and a unittest suite [Unit 6 exercice coding main.py](https://github.com/Elviix/E-portfolio/blob/main/Advanced-Object-Oriented-Design-and-Programming/Artefacts/Individual-project/Unit%206%20exercice%20coding%20main.py). This same code finally became my main artefact, improved with a Decorator, a Visitor, dependency injection and mock testing [End of module assignment code.py](https://github.com/Elviix/E-portfolio/blob/main/Advanced-Object-Oriented-Design-and-Programming/Artefacts/Individual-project/End%20of%20module%20assignment%20code.py. Following one piece of code through three stages taught me more than any reading as each version exposed a weakness of the previous one.

print(account.get_balance()) #Always 10100 never less

