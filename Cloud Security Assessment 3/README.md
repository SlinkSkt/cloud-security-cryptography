# Homomorphic Encryption & Secret Sharing

This folder contains interactive web-based implementations of **Paillier homomorphic encryption** and **Shamir Secret Sharing** schemes.

## Contents

- **paillier.html** - Interactive Paillier encryption demonstration
- **Shamir.html** - Interactive Shamir Secret Sharing implementation
- **s3894630_INTE2402-2691 Assignment 3.docx** - Report document ([View on Google Docs](https://docs.google.com/document/d/1nWa0dl6UOoso-jGlagvnEKSeGE4gaEwjLSqw0QhTFHg/edit?usp=sharing))

## Paillier Homomorphic Encryption

### Overview
An interactive HTML/JavaScript implementation of the Paillier cryptosystem demonstrating homomorphic encryption properties.

### Features
- **1024-bit public key** (n) for security
- **Homomorphic properties**: Supports addition of encrypted values
- **Randomness**: Each encryption uses a unique random value (r_i)
- **Step-by-step computation**: Shows intermediate values (t1, t2) in the encryption process

### Encryption Formula
For each message `m_i` with randomness `r_i`:
```
c_i = (g^m_i mod n²) × (r_i^n mod n²) mod n²
```

Where:
- `g = n + 1` (standard Paillier generator)
- `n²` is the modulus for encryption

### How to Use

1. Open `paillier.html` in a web browser
2. Click **"Compute Ciphertexts"** button
3. View the step-by-step encryption process for three messages:
   - `m₁ = 5486` (0x156e)
   - `m₂ = 9949` (0x26dd)
   - `m₃ = 6232` (0x1858)

### Output
The tool displays:
- Intermediate values (t1 = g^m mod n², t2 = r^n mod n²)
- Final ciphertexts (c₁, c₂, c₃) in hexadecimal format
- Complete computation steps for verification

## Shamir Secret Sharing

### Overview
An interactive implementation of Shamir's Secret Sharing scheme for securely distributing Paillier private key parameters.

### Features
- **Polynomial-based sharing**: Uses quadratic polynomial f(x) = S + a₁x + a₂x²
- **4 shares generated**: Creates shares for x = 1, 2, 3, 4
- **Threshold scheme**: Requires 3 out of 4 shares to reconstruct the secret
- **Lagrange interpolation**: Reconstructs secret using any 3 shares
- **Modular arithmetic**: Works over a prime modulus P

### How to Use

1. Open `Shamir.html` in a web browser
2. Enter the following inputs:
   - **Secret S**: The secret value to share (decimal)
   - **a1**: Student ID (e.g., 3894630)
   - **a2**: Random coefficient (decimal)
   - **Prime P**: A prime number greater than S (decimal)
3. Click **"Generate Shares"** to create 4 shares
4. Select any 3 shares from the dropdown menus
5. Click **"Reconstruct Secret"** to verify the secret can be recovered

### Share Generation
For each x ∈ {1, 2, 3, 4}:
```
share(x) = (S + a₁·x + a₂·x²) mod P
```

### Reconstruction
Uses Lagrange interpolation:
```
S = Σ (y_j × L_j(0)) mod P
```

Where L_j are Lagrange basis polynomials.

## Video Demonstrations

- **Q3 Video**: Demonstrates Paillier encryption
- **Q4 Video**: Demonstrates Shamir Secret Sharing

## Technical Details

### Technologies Used
- **HTML5** - Structure and layout
- **JavaScript** - Cryptographic computations
- **BigInt** - Arbitrary precision arithmetic for large numbers
- **CSS** - Styling and user interface

### Key Specifications
- **Paillier**: 1024-bit modulus
- **Shamir**: Supports secrets of arbitrary size (limited by prime P)
- **Modular arithmetic**: All operations performed modulo appropriate values

## Requirements

No installation required! Just open the HTML files in any modern web browser that supports:
- ES6 BigInt
- Modern JavaScript features

### Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Mathematical Background

### Paillier Cryptosystem
- **Additive homomorphism**: E(m₁) × E(m₂) = E(m₁ + m₂)
- **Semantic security**: Based on Decisional Composite Residuosity Assumption (DCRA)
- **Public key**: (n, g) where n = p × q (product of two primes)

### Shamir Secret Sharing
- **Information-theoretic security**: Shares reveal no information about the secret
- **Threshold**: (k, n) scheme where k shares are needed out of n total
- **Perfect security**: Any k-1 shares provide zero information about the secret

## Notes

- All computations use JavaScript BigInt for arbitrary precision
- The implementations are educational demonstrations
- Real-world applications would require additional security considerations
- The Paillier implementation uses a 1024-bit key for demonstration

## Author

**Zhen Xiao**

Student ID: 3894630

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

Copyright (c) 2025 Zhen Xiao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

