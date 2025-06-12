## ✅ `01-pro/README.md`


# 🧠 SEC1 – Password Hasher (01-Pro Version)

Welcome to the **Pro Version** of the Password Hasher project.  
This version introduces a clean, modular structure using Python classes and Enums.  
It is ideal for developers seeking to understand better software design, responsibility separation, and CLI tooling.

---

## 📦 Structure Overview

```

01-pro/
├── core/
│   ├── hasher.py           # HashManager class
│   └── enums.py            # Supported hashing algorithms (Enum)
│
├── utils/
│   └── io\_handler.py       # File handling logic (test mode)
│
├── main.py                 # CLI entry point
├── test\_cases.txt          # Passwords for batch testing
├── requirements.txt        # Dependencies (bcrypt)
└── README.md               # This file

````

---

## 🚀 How to Run

### 🟢 Interactive CLI Mode

```bash
python main.py
````

This will:

1. Ask you to choose a hashing algorithm (`sha256`, `sha512`, `bcrypt`)
2. Request a password input
3. Print the hash result
4. For `bcrypt`, ask to re-enter password for verification

---

### 🔁 Automated Test Mode

You can use the `--test` flag to hash all passwords from `test_cases.txt`:

```bash
python main.py --test sha256
python main.py --test sha512
python main.py --test bcrypt
```

---

## 💻 Technologies Used

* Python 3.10+
* `hashlib` (built-in)
* `bcrypt` (external)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ✅ What’s Different from the Basic Version?

| Feature                    | Basic Version | Pro Version |
| -------------------------- | ------------- | ----------- |
| Procedural Code            | ✅ Yes         | ❌ No        |
| Modular Class Structure    | ❌ No          | ✅ Yes       |
| Enum for Algorithm Control | ❌ No          | ✅ Yes       |
| CLI Test Mode              | ✅ Yes         | ✅ Yes       |
| Test File Handler          | ❌ No          | ✅ Yes       |

---

## 🧪 Example Output

```
🔐 Password Hasher – PRO Edition
Algorithm: sha256
Enter password: MyS3cret
🔒 SHA256 Hash:
49d9c0...
```

---

## 🔍 Educational Focus

* Separation of concerns (core logic vs. I/O)
* Using Enums for safe option selection
* Reusability of components
* Creating testable, extensible CLI applications

---

## 🧭 What's Next?

Go beyond hashing and move on to:

➡️ `SEC2 – Port Scanner` (Networking + Sockets)

---

> Project by Mohammad H. – VDTeam
> Part of the `#SEC-Series` 🔐


---

