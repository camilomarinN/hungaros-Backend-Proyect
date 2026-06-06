from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError
)
import os

# Configuración recomendada Argon2id
ph = PasswordHasher(
    time_cost=3,        # Iteraciones
    memory_cost=65536,  # 64 MB
    parallelism=4
)

# Pepper desde variable de entorno
PEPPER = os.environ.get("PASSWORD_PEPPER", "")

def hash_password(plain_password: str) -> str:
    """
    Genera un hash Argon2id seguro usando pepper.
    """
    pw = plain_password + PEPPER
    return ph.hash(pw)

def verify_password(stored_hash: str, plain_password: str) -> bool:
    """
    Verifica una contraseña contra un hash Argon2.
    Devuelve False ante cualquier error.
    """
    pw = plain_password + PEPPER
    try:
        return ph.verify(stored_hash, pw)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False
