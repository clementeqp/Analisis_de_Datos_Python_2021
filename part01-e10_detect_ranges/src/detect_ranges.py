#!/usr/bin/env python3

def detect_ranges(L):
    
    L=sorted(L)
    result = []
    begin, end = L[0], L[0]
    for l in L:
        if l == end:
            end += 1             
        else:
            if begin + 1 == end: 
                result.append(begin)
            else:
                result.append((begin, end))
            begin = l
            end = begin + 1
    if begin + 1 == end: 
        result.append(begin)
    else:
        result.append((begin, end))
    return result
             
    
    return Ltemp

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
