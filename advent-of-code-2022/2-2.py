scores = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]
free = [1, 2, 3]
mp = {
    'A': 0,
    'X': 0,
    'B': 1,
    'Y': 1,
    'C': 2,
    'Z': 2
}
with open("input.txt", "r") as f:
    ans = 0
    for l in f:
        move = l.strip().split()
        me = mp[move[0]]
        opponent = me
        if move[1] == 'X':
            # me lose
            if scores[opponent][(opponent + 1) % 3] == 6:
                me = (opponent + 1) % 3
            else:
                me = (opponent + 2) % 3
        elif move[1] == 'Z':
            # me win
            if scores[opponent][(opponent + 1) % 3] == 0:
                me = (opponent + 1) % 3
            else:
                me = (opponent + 2) % 3

        ans += free[me] + scores[me][opponent]
        print(ans)

