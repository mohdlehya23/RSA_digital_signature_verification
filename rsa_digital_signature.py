"""SDEV 4303 - Software Security
Chapter 02: Cryptographic Tools
RSA Digital Signature demonstration using Python 3 and the cryptography package.
"""

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_keys():
    """Generate an RSA private key and its matching public key."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key, private_key.public_key()


def sign_message(message: bytes, private_key) -> bytes:
    """Sign a message using RSA-PSS with SHA-256."""
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def verify_signature(message: bytes, signature: bytes, public_key) -> bool:
    """Return True if the signature matches the message; otherwise False."""
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False


def main():
    print("[+] Step 1: Generating RSA 2048-bit key pair...")
    alice_private_key, alice_public_key = generate_keys()

    message = b"Transfer $1000 to Mark"
    print(f"[+] Original Message: {message.decode('utf-8')}")

    signature = sign_message(message, alice_private_key)
    print(f"[+] Generated RSA Signature (first 64 hex characters): {signature.hex()[:64]}...")

    is_valid = verify_signature(message, signature, alice_public_key)
    print(f"[+] Verification on genuine message: {is_valid}")

    tampered_message = b"Transfer $1000 to Oscar"
    print(f"[!] Tampered Message: {tampered_message.decode('utf-8')}")
    is_tampered_valid = verify_signature(
        tampered_message, signature, alice_public_key
    )
    print(
        f"[!] Verification on tampered message: {is_tampered_valid} (Detected!)"
    )


if __name__ == "__main__":
    main()
