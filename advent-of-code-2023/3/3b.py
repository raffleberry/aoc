
def get_numbers(g, i, j, ni, nj):
    gv = {}
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    nums = []
    for p in range(8):
        x = i + dx[p]
        y = j + dy[p]
        if 0 <= x and x < ni:
            if 0 <= y and y < nj:
                if g[x][y].isnumeric() and (x,y) not in gv:
                    k = y
                    while k-1 >= 0 and g[x][k-1].isnumeric():
                        k -= 1
                    nstart = k
                    while k < nj and g[x][k].isnumeric() and (x,k) not in gv:
                        gv[x,k] = True
                        k += 1
                    nums.append(int(g[x][nstart:k]))
    return nums

with open("input.txt") as file:
    g = []
    v = []
    ans = 0
    for line in file:
        g.append(line.strip()) # problemo ('\n')
        v.append(len(line.strip()) * [False])
    for i, x in enumerate(g):
        for j, y in enumerate(x):
            if y == '*':
                nums = get_numbers(g, i, j, len(g), len(x))
                if len(nums) == 2:
                    ans += nums[0] * nums[1]
    print(ans)
                
                