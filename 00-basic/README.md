# 00-basic: procedural example

`hasher.py` exposes `hash_bcrypt` / `verify_bcrypt` and SHA-256/SHA-512 demonstration helpers. bcrypt is the recommended default in the CLI. SHA helpers are fast and must not be used to store passwords.

From the repository root:

```bash
python 00-basic/hasher.py
python 00-basic/hasher.py --algorithm sha256  # educational demonstration only
```

The password is entered through hidden terminal input. bcrypt output contains its own salt and cost; keep the whole encoded hash. bcrypt has a 72-byte input limit, and the API rejects longer UTF-8 inputs.

Install dependencies from the repository root with `python -m pip install -r 00-basic/requirements.txt`. Run the shared test suite as described in the root README.
