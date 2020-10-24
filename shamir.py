#!/usr/bin/python
# -*- coding: UTF-8 -*-

from binascii import hexlify, unhexlify
from Cryptodome.Protocol.SecretSharing import Shamir
from Cryptodome.Random import get_random_bytes
import sys


# Excessive, but used for better code organization. Splits unhex_P_KEY into N shares with T required to reconstruct the key.
# Returns tuples of 'int_index, unhex_share'
def split(P_KEY, N, T):
    shares = Shamir.split(T, N, P_KEY)
    return shares

# Recovers the key. 'input_strings' is an array of tuples (format is 'int_index, unhex_share'). Returns unhex_key
def recover(input_strings):
    shares = []
    for i in range(0, len(input_strings)):
        shares.append((input_strings[i][0], unhexlify(input_strings[i][1])))
    key = Shamir.combine(shares)
    return key
    
# Autotest function. By default splits random key to 3 shares with 2 sufficient to restore the key. Spams with keys and result of the test.
def autoTest(N=1):
    for j in range(0, N):
        key = get_random_bytes(16)
        shares = split(key, 3, 2)
        newshares = []
        for i in shares:
            newshares.append((i[0],hexlify(i[1])))
        newkey = recover(newshares)

        if key == newkey:
            print("Test {} passed (key: {})".format(j+1, hexlify(key)))
        else:
            print("Test {} failed (original key: {} \n                restored key: {})".format(j+1, hexlify(key), hexlify(newkey)))

# Main part of the program - no imports
if __name__ == '__main__':

    # all available modes: split, recover, autotest

    if len(sys.argv) == 1:
        print("Please specify argument (split, recover or autotest)")
        exit(1)

    if sys.argv[1] == "split":

        # unholy manipulations with input to get .Shamir working
        key = input(" Enter your key: ").encode("utf-8") 
        key = unhexlify(key)


        N, T = input(" Enter number of shares and number of shares, sufficient to reconstruct the key (separated by a whitespace symbol): ").strip().split()

        try:
            shares = split(key, int(N), int(T))
        except:
            print("Error while generating shares (key is, probably, incorrect)")

        for i in shares:
            print(i[0], hexlify(i[1]))

    if sys.argv[1] == "recover":

        n = input(" Enter given number of shares: ")  

        input_shares = []


        # getting our shares and parsing them to make combine available
        for j in range(0, int(n)):     
            i, share = input(" Enter index and share separated by a whitespace: ").split()
            input_shares.append((int(i), unhexlify(share)))

        try:
            key = Shamir.combine(input_shares)
        except:
            print("Error while combining (shares are, probably, incorrect)")

        print(hexlify(key))

    if sys.argv[1] == "autotest":

        n = input(" Enter amount of tests: ")
        autoTest(int(n))

    else:
        print("Please specify argument (split, recover or autotest)")