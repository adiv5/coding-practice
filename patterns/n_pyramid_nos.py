"""
Create a pyramid of numbers , each row contains numbers in ascending order  and ith row contains i numbers in ascending order starting from 1
"""

def create_pattern(n):
    pattern=''
    for i in range(n):
        for j in range(i+1):
            pattern+=str(j+1)
        pattern+='\n'
    print(pattern)

if __name__=='__main__':
    n=int(input())
    create_pattern(n)