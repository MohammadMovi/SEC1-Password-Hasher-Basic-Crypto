import hashlib
import bcrypt
from .enums import HashAlgorithm

class HashManager:
    def __init__(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm
    
    def hash(self, password: str) -> str:
        if self.algorithm == HashAlgorithm.SHA256:
            return hashlib.sha256(password.encode()).hexdigest()
        elif self.algorithm == HashAlgorithm.SHA512:
            return hashlib.sha512(password.encode()).hexdigest()
        elif self.algorithm == HashAlgorithm.BCRYPT:
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(password.encode(), salt).decode()
        else:
            raise ValueError("Unsupported algorithm.")    
         
    def verify(self, password: str, hashed: str) -> bool:
        if self.algorithm != HashAlgorithm.BCRYPT:
            raise NotImplementedError("Verification is only supported for bcrypt.")
        return bcrypt.checkpw(password.encode(), hashed.encode())
         