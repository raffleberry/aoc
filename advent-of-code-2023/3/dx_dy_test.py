dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

input = [
    '123',
    '456',
    '789'
]
for i in range(3):
    for j in range(3):
        for p in range(8):
            if 0 <= i + dx[p] and i + dx[p] < 3:
                if 0 <= j + dy[p] and j + dy[p] < 3:
                    print(input[i + dx[p]][j + dy[p]], end="")
        print()

# output:
# 254
# 36541
# 652
# 12587
# 23698741
# 39852
# 458
# 56974
# 685
#
# ok passed