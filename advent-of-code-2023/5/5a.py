# seed-to-soil map
# 50 98 2
# 52 50 48
# seed number 98 corresponds to soil number 50

def nex(n, lis):
    for a in lis:
        if a[1] <= n and n <= (a[1] + a[0] - 1):
            return a[2] + (n - a[1])
    return n

with open("input.txt") as file:
    inp = file.readlines()
    seeds = [int(x) for x in inp[0].split(':')[1].strip().split()]
    maps = {}
    cur = ''
    for i in inp[1:]:
        if i.strip() != "":
            if "map" in i:
                k = i.split(' map')[0].replace('to-', '')
                maps[k] = []
                cur = k
            else:
                a = [int(x) for x in i.strip().split()]
                a.reverse()
                maps[cur].append(a)
    # print(maps)
    # {'seed-soil': [[2, 98, 50], [48, 50, 52]], 'soil-fertilizer': [[37, 15, 0], [2, 52, 37], [15, 0, 39]], 'fertilizer-water': [[8, 53, 49], [42, 11, 0], [7, 0, 42], [4, 7, 57]], 'water-light': [[7, 18, 88], [70, 25, 18]], 'light-temperature': [[23, 77, 45], [19, 45, 81], [13, 64, 68]], 'temperature-humidity': [[1, 69, 0], [69, 0, 1]], 'humidity-location': [[37, 56, 60], [4, 93, 56]]}
    ans = 999999999999
    for seed in seeds:
        des = seed
        for k in maps:
            des = nex(des, maps[k])
        # print(des)
        ans = min(ans, des)
    print(ans)