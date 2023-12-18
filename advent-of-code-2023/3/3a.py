def check_for_symbol(g, i, j, ni, nj):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for p in range(8):
        if 0 <= i + dx[p] and i + dx[p] < ni:
            if 0 <= j + dy[p] and j + dy[p] < nj:
                if g[i + dx[p]][j + dy[p]] != '.' and not g[i + dx[p]][j + dy[p]].isnumeric():
                    # print(g[i][j], g[i + dx[p]][j + dy[p]])
                    return True
    return False

with open("input.txt") as file:
    g = []
    v = []
    ans = 0
    for line in file:
        g.append(line.strip()) # problemo ('\n')
        v.append(len(line.strip()) * [False])
    for i, x in enumerate(g):
        for j, y in enumerate(x):
            if g[i][j].isnumeric() and v[i][j] == False:
                k = j
                v[i][j] = True
                while k < len(x) and x[k].isnumeric():
                    v[i][k] = True
                    k += 1
                # print(x[j:k])
                near_symbol = False
                for p in range(j, k):
                    near_symbol |= check_for_symbol(g, i, p, len(g), len(x))
                # print(x[j:k], near_symbol)
                if near_symbol:
                    ans += int(x[j:k])
    print(ans)
                
                