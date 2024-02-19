# 11723

import sys; r=sys.stdin.readline
s=0
for _ in range(int(r())):
    tmp = r().split()
    if tmp[0] == 'add':
        s |= 1<<(int(tmp[1])-1)
    elif tmp[0] == 'remove':
        s &= ~(1<<(int(tmp[1])-1))
    elif tmp[0] == 'check':
        print(1 if s&(1<<(int(tmp[1])-1)) > 0 else 0)
    elif tmp[0] == 'toggle':
        s ^= 1<<(int(tmp[1])-1)
    elif tmp[0] == 'all':
        s = 0b11111_11111_11111_11111
    elif tmp[0] == 'empty':
        s = 0
