from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def hash(password: str):
    """Return hashed version of the given password."""
    return pwd_context.hash(password)


def verify(hashed_password: str, plain_text_password: str):
    """Check if plain text password matches the hashed password."""
    return pwd_context.verify(hashed_password, plain_text_password)
