count = 0
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
      line = line.strip().replace(',', '-')
      [a, b, x, y] = [int(i) for i in line.split('-')]
      count += 1 if max(a, x) <= min(b, y) else 0
    print(count)