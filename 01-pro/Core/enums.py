from enum import Enum

class HashAlgorithm(Enum):
    SHA256 = "sha256"
    SHA512 = "sha512"
    BCRYPT = "bcrypt"
