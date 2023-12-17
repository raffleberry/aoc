desired_config = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open("input.txt") as file:
    id = 1
    ans = 0
    for line in file:
        turns = line.split(":")[1].split(";")
        ok_turns = True
        for turn in turns:
            configs = turn.split(",")
            ok_config = True
            for config in configs:
                # print (config)
                count, color = int(config.strip().split(" ")[0]), config.strip().split(" ")[1]
                if not (color in desired_config and desired_config[color] >= count):
                    ok_turns = False
                    # print(color in desired_config)
                    # print(desired_config[color] <= count)
                    # print(id, color, count)
            if not ok_config:
                ok_turns = False
        if ok_turns:
            ans += id
            print(id)
        id += 1
    print(ans)