digs = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
with open("input.txt") as file:
    sum = 0
    for line in file:
        first, last = '', ''
        for i, c in enumerate(line):
            if first == '':
                if c.isnumeric():
                    first = c
                else:
                    for j, d in enumerate(digs):
                        if len(line[i:]) >= len(d):
                            if line[i: i + len(d)] == d:
                                first = f'{j}'
            else:
                break
        rline = line[::-1]
        for i, c in enumerate(rline):
            if last == '':
                if c.isnumeric():
                    last = c
                else:
                    for j, d in enumerate(digs):
                        if len(rline[i:]) >= len(d):
                            if rline[i: i + len(d)] == d[::-1]:
                                last = f'{j}'
            else:
                break
        # print(first + last)
        sum += int(first + last)

    print(sum)
    