#!/usr/bin/python3
import sys
import time
import math
"""RSA Factoring Challenge"""

def factorizer(n):
    if(n > 1):   
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                print("{}={}*{}".format(n,n//i,i))
                break
        else:
            print("{}={}*{}".format(n,n,1))

# t0 = time.time()
try:
    with open(sys.argv[1], 'r', encoding="utf-8") as file_read:
        contents = file_read.readlines()
    for content in contents:
        int_type = int(content)
        factorizer(int_type)
        # print(type(int(content)),end="")

except (FileNotFoundError, ValueError):
    pass


# t1 = time.time()
# print("Time it took: {}".format(t1-t0))