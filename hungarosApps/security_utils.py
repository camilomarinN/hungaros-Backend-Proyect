from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError
import os

ph = PasswordHasher(
    time_cost=3,       # Iteraciones
    memory_cost=65536, # 64 MB
    parallelism=4
)

PEPPER = os.environ.get("PASSWORD_PEPPER", "")

def hash_password(plain_password: str) -> str:
    pw = plain_password + PEPPER
    return ph.hash(pw)

def verify_password(stored_hash: str, plain_password: str) -> bool:
    pw = plain_password + PEPPER
    try:
        return ph.verify(stored_hash, pw)
    except (VerifyMismatchError, VerificationError):
        return False
