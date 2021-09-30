# BOJ 1874
# Python 3  34168 KB, 4080ms
# PyPy 3   151456 KB,  320ms
n=int(input())
stack=[]
c=0
ans=[]
for _ in range(n):
    i = int(input())

    while c < i:
        c+=1
        stack.append(c)
        ans.append('+')

    if stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit(0)
print(*ans, sep='\n')