with open("input.txt", "r") as f:
    c = 0
    sumans = 0
    for l in f:
        l = [int(i) for i in l.strip().split('x')]
        sl = min(l[0] * l[1], l[1] * l[2], l[2] * l[0])
        ans = 2 * (l[0] * l[1] + l[1] * l[2] + l[2] * l[0]) + sl
        sumans += ans
    print(sumans)
