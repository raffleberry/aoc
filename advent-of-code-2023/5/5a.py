with open("5a.txt") as file:
    inp = file.readlines()
    print(inp)
    seeds = [int(x) for x in inp[0].split(':')[1].strip().split()]
    maps = {}
    cur = ''
    for i in inp[1:]:
        if i.strip() != "":
            if "map" in i:
                [src, des] = i.split(' map')[0].split('-to-')
                k = f'{des}-{src}'
                maps[k] = []
                cur = k
            else:
                maps[cur].append([int(x) for x in i.strip().split()])
    print(maps)