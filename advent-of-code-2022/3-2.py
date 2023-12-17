p = {}

for i in range(ord('A'), ord('Z') + 1):
  p[chr(i)] = i - 38
  p[chr(i + 32)] = i - 38 - 26

sum = 0
with open("input.txt", "r") as f:
    common = {}
    for i, line in enumerate(f):
      line = line.strip()
      for c in set(line):
        common[c] = common.get(c, 0) + 1
      if ((i+1) % 3 == 0):
        for k in common:
          if common[k] == 3:
            sum += p[k]
            print(p[k])
        common = {}
    print(sum)
