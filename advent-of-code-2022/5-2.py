def pr(s):
  for i in s:
    print(i)
  print()

with open("5-1.input.txt") as f:
  stk = [[] for i in range(9)]
  for l in f:
    lli = l.strip().split(',')
    for i in range(9):
      if len(lli[i]) > 0:
        stk[i].append(lli[i])
  for s in stk:
    s.reverse()
  pr(stk)
  with open("5-1.moves.txt") as m:
    for l in m:
      cnt, fr, to = int(l.split()[1]), int(l.split()[3]) - 1, int(l.split()[5]) - 1
      tmp = []
      for i in range(cnt):
        tmp.append(stk[fr].pop())
      stk[to].extend(reversed(tmp))
  pr(stk)
  for s in stk:
    print(s[len(s) - 1], end='')
  print()
