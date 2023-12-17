with open("input.txt", "r") as f:
    c = 0
    for l in f:
        l = l.strip()
        for ch in l:
            if ch == "(":
                c += 1
            else:
                c -= 1
        print(c)
    print(c)

