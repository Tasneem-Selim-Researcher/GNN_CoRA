import os
import sys
import json
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import constant_time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import keywrap
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding as asym_padding
import secrets

if len(sys.argv) != 4:
    print("Usage: python encrypt_submission.py submission.csv public_key.pem submission.enc")
    sys.exit(1)

input_file = sys.argv[1]
public_key_file = sys.argv[2]
output_file = sys.argv[3]

# Load public key
with open(public_key_file, "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Generate random AES key
aes_key = secrets.token_bytes(32)
iv = secrets.token_bytes(16)

# Encrypt CSV with AES
with open(input_file, "rb") as f:
    data = f.read()

padder = sym_padding.PKCS7(128).padder()
padded_data = padder.update(data) + padder.finalize()

cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Encrypt AES key with RSA
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save everything in one file
payload = {
    "encrypted_key": base64.b64encode(encrypted_key).decode(),
    "iv": base64.b64encode(iv).decode(),
    "ciphertext": base64.b64encode(ciphertext).decode(),
}

with open(output_file, "w") as f:
    json.dump(payload, f)

print("Encryption complete →", output_file)
