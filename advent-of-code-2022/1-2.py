cur = 0
maxn = 0
top = []
with open("input.txt", "r") as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            top.append(cur)
            cur = 0
        else:
            cur += int(l)
    top.append(cur)
    top.sort(reverse=True)
    print(top[0]+ top[1]+ top[2])
