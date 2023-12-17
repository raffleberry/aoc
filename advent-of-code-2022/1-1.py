cur = 0
maxn = 0
with open("input.txt", "r") as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            maxn = max(cur, maxn)
            print("cur -", cur)
            print("maxn -", maxn)
            cur = 0
        else:
            cur += int(l)
    print(max(maxn, cur))
