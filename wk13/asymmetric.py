from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Bob's key pair generation
bob_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

bob_public_key = bob_private_key.public_key()

# Alice's key pair generation
alice_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

alice_public_key = alice_private_key.public_key()

# Message from Alice to Bob
message = b"Hello Bob, this is a secret message!"


# Encryption by Alice using Bob's public key
ciphertext = bob_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Use a valid hash algorithm
        algorithm=hashes.SHA256(),  # Use a valid hash algorithm
        label=None,
    ),
)

# Decryption by Bob using his private key
decrypted_message = bob_private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Use a valid hash algorithm
        algorithm=hashes.SHA256(),  # Use a valid hash algorithm
        label=None,
    ),
)

print(f"Original Message: {message.decode()}")
print(f"Encrypted Message: {ciphertext}")
print(f"Decrypted Message by Bob: {decrypted_message.decode()}")
