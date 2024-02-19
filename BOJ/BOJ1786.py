# 문자열 KMP 기본 문제

def makeTable(pattern):
  l=list(pattern)
  s=len(l)
  table=[0 for i in range(s)]

  j=0
  for i in range(1, s):
    while j>0 and l[i]!=l[j]:
      j=table[j-1]
    if l[i]==l[j]:
      j+=1
      table[i]=j
  return table

def KMP(parent, pattern):
  ans=[]
  table = makeTable(pattern)

  lParent = list(parent)
  lPattern = list(pattern)
  sParent = len(lParent)
  sPattern = len(lPattern)

  j=0
  for i in range(sParent):
    while j>0 and lParent[i]!=lPattern[j]:
      j=table[j-1]
    if lParent[i]==lPattern[j]:
      if j==sPattern-1:
        ans.append(i-sPattern+2)
        j=table[j]
      else:
        j+=1
  return ans

T=input()
P=input()
ans=KMP(T, P)
print(len(ans),*ans,sep='\n')
