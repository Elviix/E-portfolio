import threading
import unittest
from unittest.mock import MagicMock
from abc import ABC, abstractmethod

class BankAccount:      #class (unit 1)
    def __init__(self,owner,account_number,balance):
        self._owner = owner
        self._account_number = account_number
        self._balance = balance
        self._deposit = 0
        self._withdraw = 0
        self._penalty = 0
        self._lock = threading.Lock() # One lock per account (python docs)

    @property
    def owner(self): #encapsulation read only access
        return self._owner

    def apply_penalty(self):
        PENALTY = 5
        self._balance -= PENALTY
        self._penalty += PENALTY

    def deposit(self, amount):
        with self._lock:              # only one thread enters at a time
            if amount < 0:
                self.apply_penalty()
                return False
            self._balance += amount
            self._deposit += amount
            return True


    def withdraw(self, amount):
        with self._lock:              # locked while withdrawing

            if amount < 0:
                self.apply_penalty()
                return False

            if self._balance >= amount:
               self._balance -= amount
               self._withdraw += amount
               return True
            self.apply_penalty()    # insufficient funds =penalty
            return False

    def get_balance(self):
        with self._lock:            # even reads need locking
            return self._balance

    def transfer(self, target_account, amount):
        # always lock the account in the same order, deadlock prevention
        if self._account_number < target_account._account_number:
            first, second = self, target_account
        else:
            first, second = target_account, self

        with first._lock:
            with second._lock:
                if amount < 0:   # consistency, same validation as deposit/withdraw
                    self.apply_penalty()
                    return False
                if self._balance >= amount:
                    self._balance -= amount
                    target_account._balance += amount
                    print(f"Transferred {amount}€ from {self._owner} to {target_account._owner}")
                    return True
                self.apply_penalty()
                print(f"{self._owner} has insufficient funds,  5euro penalty applied. New balance: {self._balance} euro")
                return False

    def __str__(self):
        with self._lock:
            return (f"Owner: {self._owner}, "
                f"Account: {self._account_number}, "
                f"Balance: {self._balance} euro, "
                f"Deposit: {self._deposit}, "
                f"Withdraw: {self._withdraw}, "
                f"Penalty: {self._penalty}")

    def accept(self, visitor):   # Visitor pattern,  lets an outside algorithm read the account
        return visitor.visit_account(self)

class LoggingAccount:   # decorator pattern, adds audit log without changing BankAccount
    def __init__(self, account): # dependency injection , wrapped account is injected via the constructor
        self._account = account

    @property
    def owner(self):
        return self._account.owner

    def deposit(self, amount):
        print(f"LOG deposit {amount}")
        return self._account.deposit(amount)

    def withdraw(self, amount):
        result = self._account.withdraw(amount)
        print(f"LOG withdraw {amount} {result}")
        return result

    def get_balance(self):
        return self._account.get_balance()

    def transfer(self, target_account, amount):
        print(f"LOG transfer {amount}")
        return self._account.transfer(target_account, amount)

    def accept(self, visitor):
        return self._account.accept(visitor)

    def __str__(self):
        return str(self._account)

class AccountVisitor(ABC):  # Visitor pattern (unit 5), separates reporting from the account
    @abstractmethod
    def visit_account(self, account):
        pass

class ReportVisitor(AccountVisitor):  # analytics, builds a summary and totals all balances
    def __init__(self):
        self.total = 0

    def visit_account(self, account):
        balance = account.get_balance()
        self.total += balance
        return f"{account.owner}: {balance} euro"

class Transaction(ABC): # command pattern (unit 5), SOLID (unit 2)
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def execute(self, account):
        pass

    @abstractmethod
    def label(self):
        pass

class Deposit(Transaction):
    def execute(self, account):
        account.deposit(self.amount)

    def label(self):
        return "deposit"

class Withdraw(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)

    def label(self):
        return "withdraw"


class TransactionSimulator:#srp(unit 2)
    def __init__(self,account): #DI constructor injection
        self._account = account # the bank account that all users will share

    def user_transactions(self, user_name , transactions):
        # this runs for each user
        for transaction in transactions:
            transaction.execute(self._account) #polymorphism (unit 1)
            print(f"{user_name }, {transaction.label()}, {transaction.amount} euros, balance: {self._account.get_balance()}euro")
        print()
    def run(self):
        # define what each user will do
        users = {
            "Stephanie": [Deposit(200), Withdraw(100)],
            "Eric": [Deposit(60), Withdraw(20)],
            "Melanie": [Withdraw(150), Deposit(250)],
        }

        threads =[]
        # create one thread per user
        for user_name , transactions in users.items():
            t = threading.Thread(
                target=self.user_transactions,
                args=(user_name , transactions)
            )
            threads.append(t)

        # start all threads (users act at the same time)
        for t in threads:
            t.start()

        # wait for everyone to finish
        for t in threads:
            t.join()

        print(f"\nFinal balance (shared): {self._account.get_balance()} euro")
        print()

class TestbankAccount(unittest.TestCase): #  SRP(unit 2)
    def test_deposit(self):
        account = BankAccount("Jess",1234,100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw(self):
        account = BankAccount("Jess", 1234, 100)
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)

    def test_penalty(self):
        account = BankAccount("Lily", 7777, 50)
        account.withdraw(60)  # refused, penalty applied
        self.assertEqual(account.get_balance(), 45)  #50-5

    def test_transfer(self):
        account1 = BankAccount("Jess", 1234, 600)
        account2 = BankAccount("James", 7891, 300)
        account1.transfer(account2, 100)
        self.assertEqual(account1.get_balance(), 500)
        self.assertEqual(account2.get_balance(), 400)

    def test_negative_transfer(self): #new transfer validates like deposit/withdraw
        account1 = BankAccount("jess", 1234, 600)
        account2 = BankAccount("James", 7891, 300)
        self.assertFalse(account1.transfer(account2, -50))
        self.assertEqual(account1.get_balance(), 595) #600 -5 penalty
        self.assertEqual(account2.get_balance(), 300)

    def test_thread_safety(self):
        account = BankAccount("Shared", 9999, 0)
        threads = []
        for _ in range(100):
            t = threading.Thread(target=account.deposit, args=(10,))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(account.get_balance(), 1000)

    def test_concurrent_deposit_withdraw(self): #mixed concurrent deposits + withdrawals. final balance must be exact
        account = BankAccount("Shared", 1000, 0)
        threads = []
        for _ in range(100):
            threads.append(threading.Thread(target=account.deposit, args=(10,)))
            threads.append(threading.Thread(target=account.withdraw, args=(5,)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(account.get_balance(), 500)  # 1000 deposited, 500 withdrawn

    def test_no_deadlock_cross_transfer(self): #two accounts transfer to each other concurrently, no deadlock
        a = BankAccount("A", 1, 1000)
        b = BankAccount("B", 2, 1000)
        threads = []
        for _ in range(50):
            threads.append(threading.Thread(target=a.transfer, args=(b, 10)))
            threads.append(threading.Thread(target=b.transfer, args=(a, 10)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(a.get_balance() + b.get_balance(), 2000)  # total unchanged

    def test_withdraw_insufficient_funds(self): #withdrawal refused on insufficient funds + penalty applied
        account = BankAccount("Low", 4321, 30)
        self.assertFalse(account.withdraw(100))
        self.assertEqual(account.get_balance(), 25) # 30 - 5 penalty

    def test_decorator_keeps_balance(self):  # Decorator adds logging but behaviour is the same
        account = LoggingAccount(BankAccount("Deco", 8888, 100))
        account.deposit(50)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 130)

    def test_decorator_with_mock(self):  # Mocking test LoggingAccount in isolation, no real BankAccount
        fake_account = MagicMock()  # stand in for a real account, works because of DI
        fake_account.withdraw.return_value = True
        logged = LoggingAccount(fake_account)

        logged.deposit(50)
        fake_account.deposit.assert_called_once_with(50)  # decorator delegated correctly

        result = logged.withdraw(20)
        fake_account.withdraw.assert_called_once_with(20)
        self.assertTrue(result)  # decorator returns what the account returned

    def test_report_visitor(self):  # Visitor totals balances without changing BankAccount
        a = BankAccount("Jess", 1234, 100)
        b = BankAccount("James", 7891, 300)
        visitor = ReportVisitor()
        a.accept(visitor)
        b.accept(visitor)
        self.assertEqual(visitor.total, 400)

def main(): #SRP, demo separated from the test runner
    shared_account = BankAccount("Shared", 5555, 899)
    TransactionSimulator(shared_account).run()

    account1 = BankAccount("Jess",1234,600)
    account1.deposit(30)
    account1.withdraw(60)


    account2 = BankAccount("James",7891,300)
    account2.deposit(100)

    account3 = BankAccount("Lily",2222,50)
    account3.withdraw(60)


    accounts = [account1,account2,account3]
    for account in accounts:
        print(account)
        print("-")

    # Visitor demo, build a report and total all balances
    print("\n--- Visitor demo (report) ---")
    report = ReportVisitor()
    for account in accounts:
        print(account.accept(report))
    print(f"Total across accounts: {report.total} euro")

    #decorator demo,  same account, now with an audit log
    print("\n --- Decorator demo (logging) ---")
    logged = LoggingAccount(BankAccount("logged",6060,100)) #DI real account injected
    logged.deposit(50)
    logged.withdraw(20)
    logged.withdraw(500)   # declined
    print(f"Final balance: {logged.get_balance()} euro\n")

if __name__ == "__main__":
    main()
    unittest.main(argv=[""], exit=False)  # this line runs the tests
