"""Local, offline abuse-case tests for the password hashing examples."""

from contextlib import redirect_stdout
import importlib.util
from io import StringIO
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
PRO = REPO / "01-pro"
sys.path.insert(0, str(PRO))

from Core.hasher import HashManager

SPEC = importlib.util.spec_from_file_location("basic_hasher", REPO / "00-basic" / "hasher.py")
basic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(basic)


class LocalSecurityAbuseTests(unittest.TestCase):
    """Exercise hostile inputs against local functions; no network target is used."""

    def test_bcrypt_rejects_empty_nul_and_overlong_passwords(self):
        for password in ("", "\x00", "A" * 73, "é" * 37):
            with self.subTest(password_length=len(password)):
                with self.assertRaises(ValueError):
                    basic.hash_bcrypt(password, rounds=4)
                with self.assertRaises(ValueError):
                    HashManager(rounds=4).hash(password)

    def test_bcrypt_accepts_valid_72_byte_boundary_and_unicode(self):
        for password in ("A" * 72, "é" * 36, "päss🔐"):
            with self.subTest(password_length=len(password)):
                basic_hash = basic.hash_bcrypt(password, rounds=4)
                self.assertTrue(basic.verify_bcrypt(password, basic_hash))

                manager = HashManager(rounds=4)
                pro_hash = manager.hash(password)
                self.assertTrue(manager.verify(password, pro_hash))

    def test_bcrypt_verification_fails_closed_on_malformed_hashes(self):
        malformed_hashes = (
            None,
            b"$2b$04$not-a-text-hash",
            "",
            "x" * 10_000,
            "not-ascii-🔐",
            "$2b$99$" + "x" * 53,
        )
        for malformed in malformed_hashes:
            with self.subTest(hash_type=type(malformed).__name__, length=len(malformed) if hasattr(malformed, "__len__") else None):
                self.assertFalse(basic.verify_bcrypt("synthetic-example", malformed))
                self.assertFalse(HashManager().verify("synthetic-example", malformed))

    def test_bcrypt_cost_rejects_non_integer_and_unbounded_values(self):
        for rounds in (True, 3, 17, 4.5, "12", None):
            with self.subTest(rounds=rounds):
                with self.assertRaises(ValueError):
                    basic.hash_bcrypt("synthetic-example", rounds=rounds)
                with self.assertRaises(ValueError):
                    HashManager(rounds=rounds)

    def test_cli_does_not_echo_a_synthetic_secret(self):
        secret = "synthetic-not-a-real-password"
        output = StringIO()
        with patch.object(basic.getpass, "getpass", return_value=secret), redirect_stdout(output):
            self.assertEqual(basic.main(["--algorithm", "sha256"]), 0)
        self.assertNotIn(secret, output.getvalue())


if __name__ == "__main__":
    unittest.main()
