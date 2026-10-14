from pathlib import Path
import sys
import unittest
from unittest.mock import patch


PRO = Path(__file__).resolve().parents[1] / "01-pro"
sys.path.insert(0, str(PRO))

from Core.enums import HashAlgorithm
from Core.hasher import HashManager
import main as pro_main


class ProHasherTests(unittest.TestCase):
    def test_bcrypt_default_salts_and_verifies(self):
        manager = HashManager(rounds=4)
        first = manager.hash("synthetic-example")
        second = manager.hash("synthetic-example")
        self.assertNotEqual(first, second)
        self.assertTrue(manager.verify("synthetic-example", first))
        self.assertFalse(manager.verify("incorrect-example", first))
        self.assertFalse(manager.verify("synthetic-example", "malformed"))

    def test_sha_examples_are_explicit_and_verifiable(self):
        for algorithm in (HashAlgorithm.SHA256, HashAlgorithm.SHA512):
            manager = HashManager(algorithm)
            encoded = manager.hash("synthetic-example")
            self.assertTrue(manager.verify("synthetic-example", encoded))
            self.assertFalse(manager.verify("incorrect-example", encoded))

    def test_input_and_bcrypt_limits_are_validated(self):
        with self.assertRaises(TypeError):
            HashManager("bcrypt")
        with self.assertRaises(ValueError):
            HashManager(rounds=3)
        with self.assertRaises(ValueError):
            HashManager().hash("é" * 37)

    def test_cli_does_not_print_the_password(self):
        with patch.object(pro_main.getpass, "getpass", return_value="synthetic-example"):
            with patch("builtins.print") as output:
                self.assertEqual(pro_main.main(["--algorithm", "sha256"]), 0)
        printed = " ".join(str(call) for call in output.call_args_list)
        self.assertNotIn("synthetic-example", printed)

    def test_cli_refuses_echo_fallback(self):
        with patch.object(pro_main.getpass, "getpass", side_effect=pro_main.getpass.GetPassWarning):
            with patch("builtins.print"):
                self.assertEqual(pro_main.main(["--algorithm", "sha256"]), 2)


if __name__ == "__main__":
    unittest.main()
