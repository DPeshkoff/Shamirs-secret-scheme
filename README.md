# Shamir's Secret Scheme

Realization of Shamir's Secret Sharing Scheme. 

List of dependencies:

* Shamir from Cryptodome.Protocol.SecretSharing
* get_random_bytes from Cryptodome.Random
* hexlify, unhexlify from binascii
* sys

# Build

* Install [Python3](https://www.python.org/downloads/)
* Run `pip install pycryptodomex`to install Cryptodome
* Navigate the terminal to the directory where the script is located using the `$ cd` command.
* Type `python shamir.py` or `python3 shamir.py` in the terminal to execute the script.

# Argument types

| argument | input | output | 
| --- | --- | --- |
|  ‎ split | key, number of total shares, number of shares required to reconstruct the key  | shares | 
|  ‎ recover | amount of given shares, shares x amount | key | 
|  ‎ autotest | number of tests | test results | 

# Tests

Autotest function generates random keys, splits them into 3 shares (with 2 required for reconstruction), then reconstructs the key and compares it with the original one. 