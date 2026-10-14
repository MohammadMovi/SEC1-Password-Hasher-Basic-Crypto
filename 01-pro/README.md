# 01-pro: modular example

The modular edition provides `Core.HashManager`, which defaults to bcrypt and has explicit `hash(password)` and `verify(password, encoded_hash)` methods. Its SHA-256 and SHA-512 options exist only to compare fast hashes in an educational setting; do not use them for password storage.

From the repository root:

```bash
python 01-pro/main.py
python 01-pro/main.py --algorithm sha512  # educational demonstration only
```

The CLI hides password input and does not print or persist plaintext. bcrypt embeds a random salt and cost in the encoded hash. The API rejects UTF-8 passwords longer than bcrypt's 72-byte limit.

Install dependencies with `python -m pip install -r 01-pro/requirements.txt`. Run the shared tests from the repository root with `python -m unittest discover -s test -v`.
