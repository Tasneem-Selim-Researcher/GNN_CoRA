import os
import json
import base64
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding

if len(sys.argv) != 3:
    print("Usage: python decrypt_submission.py input.enc output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load private key from environment variable (GitHub Secret)
private_key_pem = os.environ["PRIVATE_KEY"].encode()

private_key = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
)

# Load encrypted payload
with open(input_file, "r") as f:
    payload = json.load(f)

encrypted_key = base64.b64decode(payload["encrypted_key"])
iv = base64.b64decode(payload["iv"])
ciphertext = base64.b64decode(payload["ciphertext"])

# Decrypt AES key using RSA private key
aes_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt CSV using AES
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
decryptor = cipher.decryptor()
padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding
unpadder = sym_padding.PKCS7(128).unpadder()
data = unpadder.update(padded_data) + unpadder.finalize()

# Save decrypted file
with open(output_file, "wb") as f:
    f.write(data)

print("Decryption successful →", output_file)
