#!/usr/bin/env python3

import numpy as np
"""
Propuesta
def multiplication_table(n):
    a=np.arange(n)
    return a[:, np.newaxis] * a[np.newaxis, :]
 

"""
def multiplication_table(n):
    A=np.arange(n)
    B=A.reshape(n,1)
    print(A,"\n" ,B)
    result=A*B
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
