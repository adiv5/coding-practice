"""
Creating a full inverted pyramid of stars given the no of rows
eg. n=3
*****
 ***
  *
"""

def create_pattern(n,chr):
    pattern=''
    for i in range(n):
        for j in range(i):
            pattern+=' '
        pattern+=chr*(2*(n-i-1)+1)+'\n'

    print(pattern)
    
if __name__=='__main__':
    chr='*'
    n=int(input())
    create_pattern(n,chr)

