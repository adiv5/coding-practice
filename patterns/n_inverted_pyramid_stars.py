"""
Creating an inverted pyramid of given no. of rows
eg. n=3

***
**
*
"""
def create_pattern(n,chr):
    pattern=''
    for i in range(n):
        pattern+=chr*(n-i)+'\n'
    print(pattern)

if __name__=='__main__':
    chr='*'
    n=int(input())
    create_pattern(n,chr)
