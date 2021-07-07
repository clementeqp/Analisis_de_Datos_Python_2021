#!/usr/bin/env python3
"""
def interleave(*lists):
    Ltemp=[]
    L=[]
    for item in zip(*lists):
        Ltemp.append(item)
    for i in Ltemp:
        for j in i:
            L.append(j)
        
    return L
"""
def interleave(*lists):
    L = []
    for t in zip(*lists):
        L.extend(t)
    return L

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
