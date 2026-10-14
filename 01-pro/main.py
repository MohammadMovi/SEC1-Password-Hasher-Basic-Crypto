"""Interactive CLI for the pro password-hashing example."""

import argparse
import getpass
import sys
import warnings

from Core.enums import HashAlgorithm
from Core.hasher import HashManager


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
        choices=[algorithm.value for algorithm in HashAlgorithm],
        default=HashAlgorithm.BCRYPT.value,
        help="bcrypt is recommended; SHA choices are demonstration-only",
    )
    args = parser.parse_args(argv)
    algorithm = HashAlgorithm(args.algorithm)
    manager = HashManager(algorithm)

    if algorithm != HashAlgorithm.BCRYPT:
        print("Warning: raw SHA hashes are fast and unsafe for password storage.")
    try:
        password = _prompt_password("Password: ")
        encoded = manager.hash(password)
        print(f"{algorithm.value} hash: {encoded}")
        if algorithm == HashAlgorithm.BCRYPT:
            confirmation = _prompt_password("Re-enter password to verify: ")
            print("Match." if manager.verify(confirmation, encoded) else "No match.")
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
