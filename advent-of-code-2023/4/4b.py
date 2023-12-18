def ins(ps, id, num):
    while len(ps) < id+1:
        ps.append(0)
    ps[id] += num

with open("input.txt") as file:
    ans = 0
    ps = [1]
    id = 0
    ans = 0
    for line in file:
        cards = line.strip().split(':')[1]
        [win, hav] = cards.split('|')
        win = win.strip().split()
        hav = hav.strip().split()
        won = len([x for x in hav if x in win])
        if id > 0:
            ps[id] += ps[id-1]
            ans += ps[id]
        print(id+1, f'{id+2} - {id+1+won}')
        ins(ps, id+1, ps[id]*1)
        ins(ps, id+1+won, ps[id]*-1)
        id += 1
    ps[id] += ps[id-1]
    ans += ps[id]
    print(ps)
    print(ans)        
