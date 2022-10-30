"""
Create the pyramid with each row i  containing i elements all of them are i

eg. n=3
1
22
333
"""
def create_pattern(n):
    pattern=''
    for i in range(n):
        for j in range(i+1):
            pattern+=str(i+1)
        pattern+='\n'
    print(pattern)

if __name__=='__main__':
    n=int(input())
    create_pattern(n)