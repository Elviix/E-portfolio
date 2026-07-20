# Collaborative Discussion 3 (Unit 7) – Refactoring an Authentication System with Secure Coding Practices

## Activity overview

- **Discussion topic:** Identify the vulnerabilities in an authentication code snippet and refactor it using secure practices.
- **Duration:** Unit 7.
- **Required posts:** Initial Post (≤300 words), peers reponses.

## Discussion Tasks

1. **Identify the vulnerabilities in the code:**
   - Plaintext Password Storage: passwords are stored in plaintext (no hashing/salting). Risk: if the database is compromised, attackers gain direct access to passwords.
   - SQL Injection (Logic Flaw): the `authenticate()` method compares strings directly, allowing injection (e.g., `admin' OR '1'='1` bypasses authentication).
   - Weak Password Policy: no enforcement of strong passwords (e.g., "admin123" is allowed).
   - No Input Validation: usernames/passwords are not sanitized (e.g., empty strings or malicious payloads are accepted).
   - No Rate Limiting: brute-force attacks are possible due to unlimited login attempts.
2. **Refactor with Secure Practices:**
   1. Hash Passwords (using bcrypt or argon2).
   2. Sanitise Inputs (prevent injection).
   3. Secure Authentication (compare hashes).
   4. Enforce Password Policies.
   5. Add Rate Limiting (prevent brute-force).

### Code Snippet

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        self.users.append(User(username, password))

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False


# Usage
auth_system = AuthenticationSystem()
auth_system.add_user("admin", "admin123")  # Weak password
auth_system.add_user("user1", "password")  # Weak password

# Simulate an injection attack
malicious_input = "admin' OR '1'='1"

print(auth_system.authenticate(malicious_input, "anything"))
# Output: True (Vulnerable to SQL injection)
```

## Initial Post

To avoid storing passwords in plain text which gives attackers direct access if the database is breached, used bcrypt to hash and salt every password before storing it, so only the hash is kept. 
To prevent injection and reject malformed input, I sanitised the username with a regex that only allows letters, digits and underscores. This blocks payloads like admin' OR '1'='1, because the special characters never match a stored user. 
For secure authentication, instead of comparing strings directly, I compare the entered password against the stored hash using bcrypt.checkpw(). The system never sees or compares plaintext. 
To enforce a strong password policy, I used PasswordPolicy from the password-strength library, requiring at least 12 characters, 1 uppercase letter, 1 number and 1 special character. Weak passwords like admin123 are rejected. 
To limit brute-force attacks, I capped login attempts at 5 per user; after that the account is temporarily locked 

```python
import bcrypt
import re
from password_strength import PasswordPolicy


class User:
    def __init__(self, username, password_hash):
        self._username = username
        self._password_hash = password_hash

class AuthenticationSystem:
    def __init__(self):
        self.users = {}
        self.attempts = {}
        self.policy = PasswordPolicy.from_names(length=12, uppercase=1, numbers=1, special=1)

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def add_user(self, username, password):
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
           return "Invalid username"
        if self.policy.test(password):
            return "Weak password"
        self.users[username] = User(username, self.hash_password(password))
        return "User created"

    def authenticate(self, username, password):
        if self.attempts.get(username, 0) >= 5:             # rate limiting
            return "Locked: too many attempts"
        if username not in self.users:                      # blocks injection string
            return False
        if bcrypt.checkpw(password.encode(), self.users[username]._password_hash):
            self.attempts[username] = 0
            return True
        self.attempts[username] = self.attempts.get(username, 0) + 1
        return False


# Usage
auth_system = AuthenticationSystem()
print(auth_system.add_user("admin", "admin123"))               # Weak password
print(auth_system.add_user("user1", "passwordStronger26!"))    # User created

malicious_input = "admin' OR '1'='1"
print(auth_system.authenticate(malicious_input, "anything"))   # False
print(auth_system.authenticate("user1", "passwordStronger26!"))# True
```

## Peer Response 1

*In response to a peer's refactored authentication program, which used bcrypt for hashing, the password-validator library for password strength, input validation for empty credentials, and a 3-attempt account lockout, aligned with the OWASP Top 10:*

Nice work on the refactor, the hashing and lockout parts are done well. I'd add one thing that builds on another peer's point. The original code never uses a database, so there isn't really an SQL injection to fix. The malicious input only works because of the direct string comparison in `authenticate`, which is a logic flaw rather than injection. It's worth keeping that distinction clear, since bcrypt protects stored passwords while injection is stopped at the query level with parameterised queries (OWASP, 2025). Your switch to bcrypt still helps though, because it removes the weak comparison that caused the bypass in the first place.

## Feedback Received from Peers

*Two peers reviewed my refactored code and highlighted the following:*

**Peer 1:** Good practices for password security in a simple in-memory system, especially the use of bcrypt. Even though it is based on a basic policy, just remember to include a password length cap. Bcrypt typically truncates after 72 bytes. Enforce a max length (e.g., 72–128) to prevent DoS from very long inputs. And either include an admin unlock or time-based unlock once the account is locked.

**Peer 2:** I like that you used a regular expression to validate usernames before authentication, as it helps ensure only expected characters are accepted. I also noticed you used a dictionary to store users and failed login attempts, which simplifies lookups compared to iterating through a list. Overall, your solution is well structured and easy to follow.

## References

GeeksforGeeks (2025a) *Hashing passwords in Python with bcrypt*. Available at: https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/ (Accessed: 18 June 2026).

GeeksforGeeks (2025b) *Password validation in Python*. Available at: https://www.geeksforgeeks.org/python/password-validation-in-python/ (Accessed: 18 June 2026).

Open Web Application Security Project (2025) *OWASP Top Ten Web Application Security Risks*. Available at: https://owasp.org/www-project-top-ten/ (Accessed: 4 July 2026).

Useful.codes (2025) *Python input validation and sanitization*. Available at: https://useful.codes/python-input-validation-and-sanitization/ (Accessed: 18 June 2026).
