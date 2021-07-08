#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a=np.eye(n, dtype=int)[::-1]
    b=np.eye(n, dtype=int)[:,1:]
    c=np.eye(n, dtype=int)[1::]
    d=np.eye(n, dtype=int)[::-1][1:,1:]
    ta=np.concatenate((a,b), axis=1)
    tb=np.concatenate((c,d), axis=1)
    result=np.concatenate((ta,tb))
       
    
    return result
"""
Propuesta
 
def diamond(n):
    e=np.eye(n, dtype=int)
    a=np.concatenate([e[::-1], e[:,1:]], axis=1)
    result = np.concatenate([a[:-1], a[::-1]], axis=0)
    return result

"""


def main():
    print(diamond(5))
    

if __name__ == "__main__":
    main()
