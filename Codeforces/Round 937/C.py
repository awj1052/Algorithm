import sys
r=sys.stdin.readline
 
for _ in range(int(r())):
    cmd = r().rstrip().split(":")
    h = int(cmd[0])
    m = int(cmd[1])
    time = "AM"
    if h >= 12:
        time = "PM"
        if h > 12:
            h-=12
    if h == 0:
        h = 12
    hh = str(h) if h >= 10 else "0" + str(h)
    mm = str(m) if m >= 10 else "0" + str(m)
    print(f"{hh}:{mm} {time}")