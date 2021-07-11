#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    result=a[a[:,1] > a[:,-2]]
    
    return result
    
def main():
    a=np.array([[8, 9, 3, 8, 8],
                            [0, 5, 3, 9, 9],
                            [5, 7, 6, 0, 4],
                            [7, 8, 1, 6, 2],
                            [2, 1, 3, 5, 8]])
    print(column_comparison(a))


"""
def column_comparison(a):
    mask = a[:,1] > a[:,-2]
    return a[mask]
    
def main():
    np.random.seed(0)
    a=np.random.randn(10,10)
    np.set_printoptions(linewidth=1000)
    print("a:\n", a)
    print("result:\n", column_comparison(a))

"""


if __name__ == "__main__":
    main()
