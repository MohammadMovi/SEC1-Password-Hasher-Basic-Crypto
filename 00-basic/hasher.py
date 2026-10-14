"""Basic password-hashing examples.

SHA-256 and SHA-512 are included only to demonstrate ordinary fast hashes.
Use bcrypt (or a current password-hashing standard) for stored passwords.
"""

import argparse
import getpass
import hashlib
import hmac
import sys
import warnings

import bcrypt


DEFAULT_BCRYPT_ROUNDS = 12


def _password_bytes(password: str) -> bytes:
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return password.encode("utf-8")


def hash_sha256(password: str) -> str:
    """Return a fast SHA-256 digest for demonstrations, not password storage."""
    return hashlib.sha256(_password_bytes(password)).hexdigest()


def hash_sha512(password: str) -> str:
    """Return a fast SHA-512 digest for demonstrations, not password storage."""
    return hashlib.sha512(_password_bytes(password)).hexdigest()


def hash_bcrypt(password: str, rounds: int = DEFAULT_BCRYPT_ROUNDS) -> str:
    """Hash a password with bcrypt; the encoded result includes its salt/cost."""
    raw = _password_bytes(password)
    if not 4 <= rounds <= 31:
        raise ValueError("bcrypt rounds must be between 4 and 31")
    if len(raw) > 72:
        raise ValueError("bcrypt supports at most 72 password bytes")
    return bcrypt.hashpw(raw, bcrypt.gensalt(rounds=rounds)).decode("ascii")


def verify_bcrypt(password: str, encoded_hash: str) -> bool:
    """Check a password against an encoded bcrypt hash; malformed hashes fail closed."""
    raw = _password_bytes(password)
    if not isinstance(encoded_hash, str):
        return False
    try:
        return bcrypt.checkpw(raw, encoded_hash.encode("ascii"))
    except (ValueError, TypeError, UnicodeEncodeError):
        return False


def verify_sha256(password: str, encoded_hash: str) -> bool:
    """Verify a demo-only SHA-256 digest using a constant-time comparison."""
    if not isinstance(encoded_hash, str):
        return False
    return hmac.compare_digest(hash_sha256(password), encoded_hash.lower())


def verify_sha512(password: str, encoded_hash: str) -> bool:
    """Verify a demo-only SHA-512 digest using a constant-time comparison."""
    if not isinstance(encoded_hash, str):
        return False
    return hmac.compare_digest(hash_sha512(password), encoded_hash.lower())


def _prompt_password(prompt: str) -> str:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", getpass.GetPassWarning)
            password = getpass.getpass(prompt)
    except getpass.GetPassWarning as exc:
        raise RuntimeError("This terminal cannot hide password input.") from exc
    if not password:
        raise ValueError("Password must not be empty.")
    return password


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Educational password hashing examples")
    parser.add_argument(
        "--algorithm",
        choices=("bcrypt", "sha256", "sha512"),
        default="bcrypt",
        help="bcrypt is the recommended option; SHA is for demonstration only",
    )
    args = parser.parse_args(argv)

    if args.algorithm != "bcrypt":
        print("Warning: raw SHA hashes are fast and unsafe for password storage.")
    try:
        password = _prompt_password("Password: ")
        if args.algorithm == "bcrypt":
            encoded = hash_bcrypt(password)
            print(f"bcrypt hash: {encoded}")
            confirmation = _prompt_password("Re-enter password to verify: ")
            print("Match." if verify_bcrypt(confirmation, encoded) else "No match.")
        else:
            encoded = hash_sha256(password) if args.algorithm == "sha256" else hash_sha512(password)
            print(f"{args.algorithm} digest (demo only): {encoded}")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.", file=sys.stderr)
        return 130
    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
