# Description

This is a small library aimed at the automated cryptanalysis of a two-time key cipher.

Common attacks against such cryptosystems use slow, difficult-to-automate methods such as crib-dragging. This library intends to be a replacement of such methods. We aim to provide an efficient, abstract method of retrieving the English plaintexts from an OTP cipher that reuses keystreams. This project is insipired by [this paper](https://www.cs.jhu.edu/~jason/papers/mason+al.ccs06.pdf).

# Data
Data is kept in the dat.txt file. This data is split up into training and testing sets; these will be labeled dat.train.\* and dat.test.\*, respectively. Each of these will be split into a .plain and .key file, with the encrypted file .cipher being the bitwise xor of the .plain and .key files.
