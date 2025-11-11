#Kerberos Authentication & VPN Key Exchange

This Project contains implementations of **Kerberos authentication protocol** and **Diffie-Hellman key exchange** for VPN connections.

## Contents

- **KerberosSim/** - Kerberos authentication simulation
  - `kerberos_simulation.py` - Complete Kerberos protocol implementation
  - `dh_vpn_exchange.py` - Diffie-Hellman key exchange for VPN
- **s3894630_INTE2401_2402 2691_Assi2_2025-1-1.docx** - Report document ([View on Google Docs](https://docs.google.com/document/d/12zp6Wa0SbtZeRGrWaZuydZNcfbJbglkgRxZQi-K8KAk/edit?usp=sharing))

## Kerberos Simulation

### Overview
A Python implementation of the Kerberos authentication protocol demonstrating:
- **Phase 1**: Ticket Granting Service (TGS) ticket generation
- **Phase 2**: Client authentication with the server

### Features
- AES-CBC encryption for secure ticket and authenticator transmission
- JSON-based message formatting
- Base64 encoding for binary data
- Time-based ticket lifetime management

### Configuration
- **Client**: Zhen
- **Server**: Xiao
- **Encryption**: AES-128 in CBC mode
- **Keys**: Pre-shared MD5-derived keys (K_C for client, K_S for server)

### How to Run

```bash
cd KerberosSim
python kerberos_simulation.py
```

### Output
The script generates:
1. **Phase 1**: Encrypted ticket containing session key (K_CS)
2. **Phase 2**: Encrypted authenticator with client ID and timestamp

## Diffie-Hellman VPN Key Exchange

### Overview
Implementation of Diffie-Hellman key exchange protocol for establishing secure VPN connections between:
- **VPC (Virtual Private Cloud)** - Client side (Zhen)
- **Data Centre** - Server side (Xiao)

### Features
- Large prime modulus (307-bit prime p)
- SHA-1 based secret derivation
- 160-bit random secret generation
- Shared key validation

### How to Run

```bash
cd KerberosSim
python dh_vpn_exchange.py
```

### Output
The script demonstrates:
1. Student ID-based key derivation (x = SHA1(student ID))
2. Public key computation (y = g^x mod p)
3. Diffie-Hellman key exchange between VPC and Data Centre
4. Shared secret key validation

### Key Components
- **Prime p**: 307-bit prime number
- **Generator g**: Primitive root modulo p
- **Student ID**: 3894630 (used for key derivation)
- **Random secrets**: 160-bit values for each party

## Requirements

```bash
pip install cryptography
```

## Dependencies

- `cryptography` - For AES encryption/decryption
- `hashlib` - For SHA-1 and MD5 hashing
- `secrets` - For cryptographically secure random number generation
- Standard library: `os`, `json`, `base64`, `datetime`

## Notes

- All encryption uses AES-128 in CBC mode
- Keys are derived from MD5 hashes (for simulation purposes)
- The Diffie-Hellman implementation uses large prime numbers for security
- Both implementations are educational demonstrations of cryptographic protocols

## Author

**Zhen Xiao**

Student ID: 3894630

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Zhen Xiao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

