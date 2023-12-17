p = {}

for i in range(ord('A'), ord('Z') + 1):
  p[chr(i)] = i - 38
  p[chr(i + 32)] = i - 38 - 26

sum = 0
with open("input.txt", "r") as f:
    for line in f:
      line = line.strip()
      half = len(line) // 2
      l, r = line[:half], line[half:]
      duplicate = {}
      cursum = 0
      for c in l:
        duplicate[c] = True
      makesum = {}
      for c in r:
        if duplicate.get(c):
          makesum[p[c]] = True
      for k in makesum.keys():
        cursum += k
      print(cursum)
      sum += cursum
    print(sum)
      
      # print(line + " = " + l + " + " + r)
