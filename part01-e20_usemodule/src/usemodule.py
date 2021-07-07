#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    c1, c2 = 3, 4
    print(triangle.hypothenuse(c1,c2))
    print(triangle.area(c1, c2))

if __name__ == "__main__":
    main()
