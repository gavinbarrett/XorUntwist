# Description

This is a small library aimed at the automated cryptanalysis of a two-time key cipher.

Common attacks against such cryptosystems use slow, difficult-to-automate methods such as crib-dragging. This library intends to be a replacement of such methods. We aim to provide an efficient, abstract method of retrieving the English plaintexts from an OTP cipher that reuses keystreams. This project is insipired by [this paper](https://www.cs.jhu.edu/~jason/papers/mason+al.ccs06.pdf).

![](https://github.com/gavinbarrett/XorUntwist/workflows/Probability%20Test/badge.svg)

# Data
## Source
Data is kept in the dataset/dat.tag file, which is built with the parse\_html.py script on a set of 19,000+ blog posts pulled from [here](http://www.cs.biu.ac.il/~koppel/blogs/blogs.zip). 

## Processing
Since the data is extracted sequentially, we do not want to split our data before mixing it. The first step is to break our dat.tag file into multiple chunks and zip them together. We then split the data in half, the first half will be our plaintext data, stored in dat.plain.\* files; these are split into train and test sets by a ratio specified in the split\_data.py script. The second half of our data, stored in dat.key, is the cipher key used to produce the ciphertext stored in dat.cipher.
