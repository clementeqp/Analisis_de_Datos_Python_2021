#!/usr/bin/env python3

def reverse_dictionary(d):
    dr={}
    for key, valor in d.items():
        for i in valor:
            if i in dr:
                dr[i].append(key)
            else:
                dr[i]=[key]
    return dr

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
