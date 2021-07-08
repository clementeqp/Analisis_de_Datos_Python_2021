#!/usr/bin/env python3

def extract_numbers(s):
    result =[]
    lista=s.split()
    for l in lista:
        try:
            result.append(int(l))
        except ValueError:
            try:
                result.append(float(l))
            except Exception:
                continue
    
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
