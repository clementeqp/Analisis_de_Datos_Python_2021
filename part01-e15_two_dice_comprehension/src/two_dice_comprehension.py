#!/usr/bin/env python3

def main():
    G=((a,b) for a in range(1, 7) for b in range(1, 7) if a + b == 5)
    for x in G:
        print(x)
        
    #propuesta
    # print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))
     
        
if __name__ == "__main__":
    main()
