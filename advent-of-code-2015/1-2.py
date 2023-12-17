with open("input.txt", "r") as f:
    c = 0
    for l in f:
        l = l.strip()
        i = 0
        for ch in l:
            i += 1
            if ch == "(":
                c += 1
            else:
                c -= 1
            if c == -1:
                print(c, i)
    print(c)

