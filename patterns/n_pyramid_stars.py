"""
Creating a pyramid of stars given the no of rows
eg. n=3
*
**
***

"""


def create_pattern(n,chr):
    pattern=''
    for i in range(n):
        pattern+=chr*(i+1)+'\n'
    print(pattern)


if __name__=="__main__":
    chr='*'
    n=int(input())
    create_pattern(n,chr)