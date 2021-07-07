#!/usr/bin/env python3


def main():
    for i in range(1,11):
        for j in range(1,11):
            print('{:4}'.format(i*j), end="")
        print()
        
def main_solucion():
    for r in range(1, 11):
        for c in range(1, 11):
            print(f"{r*c:4d}", end="")
        print()

if __name__ == "__main__":
    main()
