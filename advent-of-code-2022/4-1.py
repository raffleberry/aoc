count = 0
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
      line = line.strip().replace(',', '-')
      [a, b, x, y] = [int(i) for i in line.split('-')]

      if b-a < y-x:
        a, b, x, y = x, y, a, b
      
      if a <= x and y <= b:
        count += 1
    print(count)