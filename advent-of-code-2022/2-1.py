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
        ans += free[mp[move[1]]] + scores[mp[move[1]]][mp[move[0]]]
        print(ans)

