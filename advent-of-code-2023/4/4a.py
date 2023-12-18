with open("input.txt") as file:
    ans = 0
    for line in file:
        cards = line.strip().split(':')[1]
        [win, hav] = cards.split('|')
        win = win.strip().split()
        hav = hav.strip().split()
        won = len([x for x in hav if x in win])
        if won > 0:
            ans += 2**(won-1)
    print(ans)        
