# RSA Digital Signature Implementation

A Python implementation demonstrating cryptographic digital signatures using **RSA-PSS** (Probabilistic Signature Scheme) and **SHA-256**, built with Python's standard cryptography library.

---

## Overview

A digital signature provides three fundamental security properties:

1. **Authentication:** Proves that the message was created by a known sender holding the private key.
2. **Integrity:** Guarantees that the message has not been altered in transit.
3. **Non-repudiation:** The signer cannot deny having signed the message.

### Why RSA-PSS?

This implementation uses **RSA-PSS (Padding Scheme: Probabilistic Signature Scheme)** with **SHA-256** and **MGF1 (Mask Generation Function 1)**:

- Unlike deterministic padding (PKCS#1 v1.5), RSA-PSS includes randomized salt, making it provably secure against chosen-message attacks.
- Recommended by modern cryptographic standards (NIST, RFC 8017).

---

## Repository Structure

```text
├── rsa_digital_signature.py   # Main Python script for key generation, signing, and verification
├── requirements.txt           # Project dependencies (cryptography)
└── README.md                  # Project documentation and instructions
```

---

## Prerequisites & Installation

Ensure you have **Python 3.8+** installed on your system.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohdlehya23/RSA_digital_signature_verification.git
   cd RSA_digital_signature_verification
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Script

Execute the Python script:

```bash
python rsa_digital_signature.py
```

### Expected Output:

```text
[+] Step 1: Generating RSA 2048-bit key pair...
[+] Original Message: Transfer $1000 to Mark
[+] Generated RSA Signature (first 64 hex characters): <signature_hex>...
[+] Verification on genuine message: True
[!] Tampered Message: Transfer $1000 to Oscar
[!] Verification on tampered message: False (Detected!)
```

---

## How It Works

1. **Key Generation:** Generates a 2048-bit RSA private key and extracts the corresponding public key.
2. **Signing (`sign_message`):**
   - Computes the SHA-256 hash of the message.
   - Applies RSA-PSS padding with `MGF1(SHA-256)` and maximum salt length.
   - Encrypts the padded hash using the private key to form the digital signature.
3. **Verification (`verify_signature`):**
   - Decrypts/verifies the signature using the sender's public key.
   - Compares the resulting hash against the recomputed hash of the received message.
   - Returns `True` if valid, or catches `InvalidSignature` and returns `False` if tampered with.

---

## 👤 Author

- **GitHub:** [@mohdlehya23](https://github.com/mohdlehya23)
