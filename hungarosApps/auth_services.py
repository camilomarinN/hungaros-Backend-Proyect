from .models import Usuarios
from .security_utils import verify_password, hash_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def authenticate_user(id_usuario: str, plain_password: str):
    id_usuario = id_usuario.strip()
    plain_password = plain_password.strip()

    try:
        usuario = Usuarios.objects.get(id_usuario=id_usuario)
    except Usuarios.DoesNotExist:
        return None

    stored_password = (usuario.hash_contrasena_usu or "").strip()

    # Caso 1: contraseña Argon2
    if stored_password.startswith("$argon2"):
        if not verify_password(stored_password, plain_password):
            return None

    # Caso 2: usuario legacy
    elif stored_password == plain_password:
        usuario.hash_contrasena_usu = hash_password(plain_password)
        usuario.save(update_fields=["hash_contrasena_usu"])

    else:
        return None

    return usuario


def get_or_create_shadow_user(usuario):
    django_user, _ = User.objects.get_or_create(
        username=usuario.id_usuario,
        defaults={
            "is_active": True,
            "is_staff": False,
        }
    )
    return django_user


def create_single_session_token(usuario):

    django_user = get_or_create_shadow_user(usuario)

    Token.objects.filter(user=django_user).delete()

    token = Token.objects.create(user=django_user)

    return token
