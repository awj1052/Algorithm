from functools import cmp_to_key
import sys

class person:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def compare(a, b):
    if a.number%2 == b.number%2:
        if a.number > b.number:
            return 1
        elif a.number < b.number:
            return -1
        else:
            if len(a.name) > len(b.name):
                return 1
            elif len(a.name) < len(b.name):
                return -1
            else:
                if a.name > b.name:
                    return 1
                else:
                    return -1
    elif a.number%2 == 0: # a 짝 b 홀
        return 1
    else: # a 홀 b 짝
        return -1


a = []
N, M = [int(i) for i in sys.stdin.readline().split()]
count = [0 for _ in range(N+1)]
while True:
    num, name = sys.stdin.readline().split()
    if num == "0" and name == "0":
        break
    num = int(num)
    if count[num] < M:
        a.append(person(num, name))
        count[num]+=1
    
a = sorted(a, key=cmp_to_key(compare))

for i in a:
    print(i.number, i.name)