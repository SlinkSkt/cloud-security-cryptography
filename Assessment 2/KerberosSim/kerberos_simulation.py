import hashlib, os, json
from base64 import b64encode, b64decode
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# AES functions
def aes_encrypt_cbc(key: bytes, plaintext: bytes) -> tuple:
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded) + encryptor.finalize()
    return iv, ct

def aes_decrypt_cbc(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()

# Convert MD5 string (hex) to 16-byte key
def md5_bytes(hexstr: str) -> bytes:
    return bytes.fromhex(hexstr)

# Constants
C = "Zhen"
S = "Xiao"
K_C = md5_bytes("45e084d2fc570dc7f3ccf92b9a7f9bc2")
K_S = md5_bytes("13e527a9a167d774a58e8012f09a2207")
n_C = md5_bytes("3ef3a4e85e7e449999cc3d92c2dd5cfc")
L_t = str((datetime.now() + timedelta(hours=8)).isoformat())

# Phase 1
def phase1():
    K_CS = os.urandom(16)

    ticket = {
        "K_CS": b64encode(K_CS).decode(),
        "Client_ID": C,
        "Lifetime": L_t
    }
    ticket_json = json.dumps(ticket).encode()
    iv_t, enc_ticket = aes_encrypt_cbc(K_S, ticket_json)

    client_data = {
        "K_CS": b64encode(K_CS).decode(),
        "Server": S,
        "Lifetime": L_t,
        "Ticket": b64encode(enc_ticket).decode(),
        "IV_Ticket": b64encode(iv_t).decode()
    }
    client_json = json.dumps(client_data).encode()
    iv_c, enc_to_client = aes_encrypt_cbc(K_C, client_json)

    return {
        "K_CS": K_CS,
        "IV_Client": b64encode(iv_c).decode(),
        "Encrypted_Response_Client": b64encode(enc_to_client).decode(),
        "IV_Ticket": b64encode(iv_t).decode(),
        "Encrypted_Ticket": b64encode(enc_ticket).decode()
    }

# Phase 2
def phase2(K_CS):
    timestamp = datetime.now().isoformat()
    authenticator = {
        "Client_ID": C,
        "Timestamp": timestamp
    }
    auth_json = json.dumps(authenticator).encode()
    iv_auth, enc_auth = aes_encrypt_cbc(K_CS, auth_json)

    return {
        "IV_Authenticator": b64encode(iv_auth).decode(),
        "Encrypted_Authenticator": b64encode(enc_auth).decode()
    }

# Run simulation
p1 = phase1()
p2 = phase2(p1["K_CS"])

print(" Phase 1 Output (Encrypted Ticket):")
print(p1["Encrypted_Ticket"])
print("\n Phase 2 Output (Encrypted Authenticator):")
print(p2["Encrypted_Authenticator"])
