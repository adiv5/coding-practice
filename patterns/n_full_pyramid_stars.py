"""
Creating a full pyramid of stars given the no of rows
eg. n=3
  *
 ***
*****
"""
def create_pattern(n,chr):
    pattern=''
    for i in range(n):
        for j in range(n-i):
            pattern+=' '
        pattern+=chr*(2*i+1)+'\n'
    print(pattern)
        
if __name__=='__main__':
    chr='*'
    n=int(input())
    create_pattern(n,chr)

