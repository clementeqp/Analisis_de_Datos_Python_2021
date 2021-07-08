#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    filas =[]
    for i in range(a.shape[0]):
        filas.append(a[i])
    
    return filas

def get_columns(a):
    b=a.T
    
    return get_rows(b)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))
"""
propuesta

def get_rows(a):
    result = [row for row in a]
    return result
 
def get_columns(a):
    result = [row for row in a.T]
    return result

"""
if __name__ == "__main__":
    main()
