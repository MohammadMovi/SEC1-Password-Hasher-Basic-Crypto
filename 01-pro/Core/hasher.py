"""Configurable password hashing API used by the pro example."""

import hashlib
import hmac

import bcrypt

from .enums import HashAlgorithm


DEFAULT_BCRYPT_ROUNDS = 12


class HashManager:
    """Hash and verify passwords with one explicitly selected algorithm.

    bcrypt is the secure default. SHA-256 and SHA-512 are intentionally retained
    as fast-hash demonstrations and must not be used for password storage.
    """

    def __init__(
        self,
        algorithm: HashAlgorithm = HashAlgorithm.BCRYPT,
        rounds: int = DEFAULT_BCRYPT_ROUNDS,
    ) -> None:
        if not isinstance(algorithm, HashAlgorithm):
            raise TypeError("algorithm must be a HashAlgorithm")
        if not 4 <= rounds <= 31:
            raise ValueError("bcrypt rounds must be between 4 and 31")
        self.algorithm = algorithm
        self.rounds = rounds

    @staticmethod
    def _password_bytes(password: str) -> bytes:
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        return password.encode("utf-8")

    def hash(self, password: str) -> str:
        """Return an encoded password hash, including salt and parameters."""
        raw = self._password_bytes(password)
        if self.algorithm == HashAlgorithm.BCRYPT:
            if len(raw) > 72:
                raise ValueError("bcrypt supports at most 72 password bytes")
            return bcrypt.hashpw(raw, bcrypt.gensalt(rounds=self.rounds)).decode("ascii")
        if self.algorithm == HashAlgorithm.SHA256:
            return hashlib.sha256(raw).hexdigest()
        if self.algorithm == HashAlgorithm.SHA512:
            return hashlib.sha512(raw).hexdigest()
        raise ValueError(f"Unsupported algorithm: {self.algorithm}")

    def verify(self, password: str, encoded_hash: str) -> bool:
        """Verify against a hash produced for this manager's selected algorithm."""
        raw = self._password_bytes(password)
        if not isinstance(encoded_hash, str):
            return False
        if self.algorithm == HashAlgorithm.BCRYPT:
            try:
                return bcrypt.checkpw(raw, encoded_hash.encode("ascii"))
            except (ValueError, TypeError, UnicodeEncodeError):
                return False
        if self.algorithm == HashAlgorithm.SHA256:
            expected = hashlib.sha256(raw).hexdigest()
        elif self.algorithm == HashAlgorithm.SHA512:
            expected = hashlib.sha512(raw).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")
        return hmac.compare_digest(expected, encoded_hash.lower())
