#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    l = re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
    lista=list(map(int, l))
    return lista
    
    #return [int(x) for x in list]

def main():
    result=integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx")
    print(result)


if __name__ == "__main__":
    main()
