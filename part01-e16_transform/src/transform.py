#!/usr/bin/env python3

def transform(s1, s2):
    s1=s1.split()
    s2=s2.split()
    G=[x*y for (x,y) in zip(map(int,s1), map(int,s2))]
    return G
    # return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]


def main():
    s1="1 5 3"
    s2="2 6 -1"
    print(transform(s1,s2))
    
    

if __name__ == "__main__":
    main()
