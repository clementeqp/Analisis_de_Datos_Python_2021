#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    A = np.sum(X*Y, axis=1)
    B = np.sqrt(np.sum(np.square(X), axis=1)) * np.sqrt(np.sum(np.square(Y), axis=1))
    return np.degrees(np.arccos(np.clip(A/B, -1.0, 1.0)))

def main():
    A=np.random.randint(0,10,(4,5))
    #print(A)
    B=np.random.randint(0,10,(4,5))
    #print(B)
    print(vector_angles(A,B))
    

"""
import numpy as np
import scipy.linalg
 
def vector_angles(X, Y):
    ip = np.sum(X*Y, axis=1)
    Xlen = scipy.linalg.norm(X, 2, axis=1)
    Ylen = scipy.linalg.norm(Y, 2, axis=1)
    temp=ip/(Xlen*Ylen)
    temp = np.clip(temp, -1.0, 1.0)
    result =  np.arccos(temp) / np.pi * 180
    return result
 
def main():
    np.random.seed(0)
    X=np.random.randn(10,3)
    Y=np.random.randn(10,3)
    print(vector_angles(X, Y))
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(A, B))

"""


if __name__ == "__main__":
    main()
