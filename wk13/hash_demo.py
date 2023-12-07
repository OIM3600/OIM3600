import hashlib


password = "banana"
salt = "college"

hashed = hashlib.sha256((password + salt).encode()).hexdigest()

print(hashed)
