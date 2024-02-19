# BOJ 15916

input();n=[int(i) for i in input().split()];k=int(input())
if n[0]==k: print('T');exit()
for i in range(1,len(n)):
    if (n[i-1]-k*i)*(n[i]-k*(i+1)) <= 0:
        print('T')
        exit()
print('F')
