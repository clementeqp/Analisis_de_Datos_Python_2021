#!/usr/bin/env python3

def triple(n):
    return n*3

def square(n):
    return n**2
    
def main():
    for i in range(1,11):
        t=triple(i)
        s=square(i)
        if s>t:
            break
        #print("triple(%d)==%d square(%d)==%d" % (i, t,i,s))
        print("triple({0})=={1} square({0})=={2}".format(i, t, s))
        


if __name__ == "__main__":
    main()
