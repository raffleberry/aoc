with open("input.txt") as file:
    sum = 0
    for line in file:
        first = next((x for x in line if x.isnumeric()), '0')
        last = next((x for x in reversed(line) if x.isnumeric()), '0')
        sum += int(first + last)

    print(sum)
    