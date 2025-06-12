# 🔐 SEC1 – Password Hasher (00-Basic Version)

This is the **basic version** of the `SEC1 – Password Hasher` project.  
It provides a simple CLI tool to hash passwords using various common algorithms and verify them (especially with `bcrypt`).  
This version also includes an **automated test mode** to hash a list of passwords from file.

---

## 🎯 Features

- Supports three popular hashing algorithms:
  - `SHA256`
  - `SHA512`
  - `bcrypt` (with salt + verification)
- Interactive CLI mode
- Optional automated test mode for batch hashing
- Clean and easy-to-read code written in Python 3

---

## 🧪 Test Mode

You can run this version in test mode to hash multiple passwords from the `test/test_cases.txt` file.

### 🔧 Usage:

```bash
python hasher.py --test sha256
python hasher.py --test sha512
python hasher.py --test bcrypt
````

> Each line in the test file will be hashed and printed using the selected algorithm.

---

## 💻 Interactive CLI Mode

To run the standard interactive mode:

```bash
python hasher.py
```

### You'll be able to:

* Select a hashing algorithm
* Enter a password
* View the hash result
* (Optional for bcrypt) Enter password again to verify

---

## 📁 File Structure

```
00-basic/
├── hasher.py              # Main script with CLI and test mode
├── requirements.txt       # External package list (only bcrypt)
├── README.md              # This documentation
└── test_cases.txt         # Passwords for use in --test mode

../test/
└── test_cases.txt         # Central test file (shared across versions)
```

---

## 📦 Dependencies

```bash
pip install -r requirements.txt
```

* Python 3.10+
* `bcrypt` library (used for salted hashes)

---

## 🧠 Concepts Covered

* Hash vs. Encryption 🔒
* Salted hashes & rainbow table protection 🌈
* One-way hashing verification (especially for login systems)
* Hashing best practices for password storage

---

## 🧭 What's Next?

Ready to level up?
Move on to the [`01-pro/`](../01-pro/) folder to see a more modular and scalable version of this tool – written with better structure and reusability in mind.

---

> Developed by Mohammad H. – VDTeam
> Part of the `#SEC-Series` 🔐




