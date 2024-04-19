import base64
import hashlib


def hash_password_hex(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def hash_password_base64(password):
    hashed_password_in_bytes = hashlib.sha256(password.encode()).digest()
    hashed_password = base64.b64encode(hashed_password_in_bytes).decode("utf-8")
    return hashed_password


password = "cherry"
salt = 'computer'
hashed_password = hash_password_hex(password+salt)

print(f"password: {password}")
print(f"After hashing: {hashed_password}")
