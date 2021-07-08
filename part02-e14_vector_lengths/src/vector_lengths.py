#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a), axis=1))
"""
 return scipy.linalg.norm(a, 2, axis=1)
    return np.sqrt(np.sum(a**2, axis=1))

"""    
    

def main():
    a = np.random.randint(0,10,(2,3))
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
