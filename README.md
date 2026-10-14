# SEC1 — Password Hashing Basics

A small Python learning project that compares ordinary cryptographic hashes with a password-hashing function. It contains a procedural example (`00-basic/`), a modular API and CLI (`01-pro/`), and automated tests (`test/`).

## What's in this repository

```text
00-basic/       Procedural API and interactive CLI
01-pro/         HashManager API and interactive CLI
test/           unittest suite using synthetic example values
```

The repository does not currently contain `02-reverse/` or `screenshots/`; those folders are not part of the project or its setup instructions.

## Security guidance

- **Use bcrypt for password storage examples.** It generates a random salt for every hash and stores the salt and cost in the encoded hash. Save that complete encoded string; do not generate or store a separate salt.
- **SHA-256 and SHA-512 here are demonstrations only.** They are deliberately fast and unsuitable for password storage. Salting a fast hash does not make it an appropriate password-hashing scheme.
- This is educational code, not a complete authentication system. A real service should use a maintained password-hashing library and current deployment guidance, support rehashing when parameters change, protect its database and transport, and add account-level controls.
- bcrypt accepts at most 72 UTF-8 bytes. This project rejects longer inputs rather than silently truncating them. Choose a different standard password-hashing scheme if your application needs longer passwords.
- CLI passwords are read with Python's `getpass` and are not printed or saved. Do not put real passwords in command arguments, test fixtures, logs, or screenshots.
- There are no reverse/cracking experiments in this repository. Any future exercise in that area must use synthetic data offline; this project does not include keylogging or account-attack functionality.

## Requirements

- Python 3.10 or newer
- `bcrypt` (see each version's `requirements.txt`)

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r 00-basic/requirements.txt
```

## Run a CLI

From the repository root:

```bash
python 00-basic/hasher.py
python 00-basic/hasher.py --algorithm bcrypt
python 01-pro/main.py
python 00-basic/hasher.py --algorithm sha256
python 01-pro/main.py --algorithm sha512
```

bcrypt is the default. The optional `--algorithm sha256` and `--algorithm sha512` choices print a warning and are for learning only. Password input is hidden; bcrypt mode asks for a second hidden entry to demonstrate verification.

## Run the automated tests

From the repository root, after installing bcrypt:

```bash
python -m unittest discover -s test -v
```

The tests use synthetic values defined in test code. No real password fixture files are needed.

## License

MIT. See [LICENSE](LICENSE).
