#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n==0:
        return np.eye(a.shape[0])
    if n<0:
        a = np.linalg.inv(a)
        n *= -1
    l = [a for i in range(n)]
    return reduce(lambda x, y: x@y, l)

def main():
    a = np.array([[1, 6, 7],
                  [7, 8, 1],
                  [5, 9, 8]])
    print(matrix_power(a, 2))


"""
def matrix_power(a, n):
    if n >= 0:
        return reduce(np.matmul, (a for _ in range(n) ), np.eye(a.shape[0]))
    else:
        inv = np.linalg.inv(a)
        return reduce(np.matmul, (inv for _ in range(-n) ))
 
def main():
    a = np.array([[1,2], [3,4]])
    for n in range(-2,3):
        print(f"Power of {n}\n{matrix_power(a, n)}")

"""


if __name__ == "__main__":
    main()
