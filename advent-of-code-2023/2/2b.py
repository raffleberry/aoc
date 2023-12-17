with open("input.txt") as file:
    id = 1
    ans = 0
    for line in file:
        turns = line.split(":")[1].split(";")
        min_balls = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for turn in turns:
            configs = turn.split(",")
            for config in configs:
                count, color = int(config.strip().split(" ")[0]), config.strip().split(" ")[1]
                min_balls[color] = max(min_balls[color], count)
        power = 1
        for color in min_balls:
            power *= min_balls[color]
        ans += power
        # print(power, min_balls)
        id += 1
    print(ans)