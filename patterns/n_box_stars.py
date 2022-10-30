"""
Creating a pattern of n lines with m columns of stars
eg n=3 m=2
**
**
**
"""
def create_pattern(n,m,chr):
    pattern=''
    for i in range(n):
        for j in range(m):
            pattern+=chr
        pattern+='\n'

    print(pattern)



if __name__=='__main__':
    chr='*'
    n,m=int(input()),int(input())
    create_pattern(n,m,chr)