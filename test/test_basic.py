import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("basic_hasher", REPO / "00-basic" / "hasher.py")
basic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(basic)


class BasicHasherTests(unittest.TestCase):
    def test_raw_sha_examples_match_standard_vectors(self):
        sha256 = basic.hash_sha256("synthetic-example")
        sha512 = basic.hash_sha512("synthetic-example")
        self.assertEqual(
            sha256,
            "b6e084b4593937ef8a525cbe5e75e4e1217fea392bdfbb5154422050edfa7529",
        )
        self.assertEqual(
            sha512,
            "9b6970766d3023a70dad6e45cdac44ea4c146a3975d7ca02e3b946d503055409af8e9a8adf40ea33250778d1f0dae53fc76719a3d6de2b5f94e7796389a276f7",
        )
        self.assertTrue(basic.verify_sha256("synthetic-example", sha256))
        self.assertFalse(basic.verify_sha256("incorrect-example", sha256))
        self.assertTrue(basic.verify_sha512("synthetic-example", sha512))
        self.assertFalse(basic.verify_sha512("incorrect-example", sha512))

    def test_bcrypt_hash_contains_salt_and_verifies(self):
        first = basic.hash_bcrypt("synthetic-example", rounds=4)
        second = basic.hash_bcrypt("synthetic-example", rounds=4)
        self.assertNotEqual(first, second)
        self.assertTrue(basic.verify_bcrypt("synthetic-example", first))
        self.assertFalse(basic.verify_bcrypt("wrong-example", first))
        self.assertFalse(basic.verify_bcrypt("synthetic-example", "not-a-hash"))

    def test_bcrypt_rejects_overlong_utf8_password_and_bad_cost(self):
        with self.assertRaises(ValueError):
            basic.hash_bcrypt("é" * 37, rounds=4)
        with self.assertRaises(ValueError):
            basic.hash_bcrypt("synthetic-example", rounds=3)

    def test_cli_reads_hidden_input_and_does_not_print_it(self):
        with patch.object(basic.getpass, "getpass", return_value="synthetic-example"):
            with patch("builtins.print") as output:
                self.assertEqual(basic.main(["--algorithm", "sha256"]), 0)
        printed = " ".join(str(call) for call in output.call_args_list)
        self.assertNotIn("synthetic-example", printed)

    def test_cli_refuses_echo_fallback(self):
        with patch.object(basic.getpass, "getpass", side_effect=basic.getpass.GetPassWarning):
            with patch("builtins.print"):
                self.assertEqual(basic.main(["--algorithm", "sha256"]), 2)


if __name__ == "__main__":
    unittest.main()
