map = []
f = open("puzzle.input","r")

start_i=0
start_j=0
start_direction = ""
start_direction_i = 0
start_direction_j = 0

count = 0
for line in f:
    line = line.strip()
    if ">" in line or "<" in line or "^" in line or "v" in line:
        start_i = count
        if ">" in line:
            start_direction = ">"
            start_direction_i = 0
            start_direction_j = 1
        if "v" in line:
            start_direction = "v"
            start_direction_i = 1
            start_direction_j = 0
        if "<" in line:
            start_direction = "<"
            start_direction_i = 0
            start_direction_j = -1
        if "^" in line:
            start_direction = "^"
            start_direction_i = -1
            start_direction_j = 0
        start_j = line.index(start_direction)
        print(f"STARTING: {start_i},{start_j},{start_direction}")
    map.append(list(line.rstrip()))
    count += 1

# i,j is starting position and direction is the direction

# Visit the map fisst to limit our search`
i = start_i
j = start_j
direction = start_direction
direction_i = start_direction_i
direction_j = start_direction_j
map[i][j] = "X"

# while its on the map...
while i >= 0 and i < len(map[0]) and j >= 0 and j < len(map):
    new_i = i + direction_i
    new_j = j + direction_j
    if new_i < 0 or new_j < 0 or new_i == len(map[0]) or new_j == len(map):
        # off the map
        break
    if map[new_i][new_j] == "#":
        # hit an obstruction, turn right
        if direction_i == 1:
            direction_i = 0
            direction_j = -1
        elif direction_i == -1:
            direction_i = 0
            direction_j = 1
        elif direction_j == 1:
            direction_i = 1
            direction_j = 0
        elif direction_j == -1:
            direction_i = -1
            direction_j = 0
    else:
        i = new_i
        j = new_j
        map[i][j] = "X"


number_of_places = 0
for o_i in range(len(map)):
    print(f"Obstructions in line {o_i}")
    for o_j in range(len(map[0])):
        # Check every place where an obstruction can be placed
        if map[o_i][o_j] == "X":
            map[o_i][o_j] = "#"
            # track the directions at which we have visited each place. when we hit a position, going the same direction we have a loop
            positions = []
            for x in range(len(map)):
                pos_line = []
                for y in range(len(map[0])):
                    pos_line.append([])
                positions.append(pos_line)
            i = start_i
            j = start_j
            direction = start_direction
            direction_i = start_direction_i
            direction_j = start_direction_j

            # while its on the map...
            loop = False
            while not loop:
                new_i = i + direction_i
                new_j = j + direction_j
                if new_i < 0 or new_j < 0 or new_i == len(map[0]) or new_j == len(map):
                    # off the map
                    break
                if map[new_i][new_j] == "#":
                    # hit an obstruction, turn right
                    if direction_i == 1:
                        direction_i = 0
                        direction_j = -1
                        direction = "<"
                    elif direction_i == -1:
                        direction_i = 0
                        direction_j = 1
                        direction = ">"
                    elif direction_j == 1:
                        direction_i = 1
                        direction_j = 0
                        direction = "v"
                    elif direction_j == -1:
                        direction_i = -1
                        direction_j = 0
                        direction = "^"
                else:
                    i = new_i
                    j = new_j
                    if direction in positions[i][j]:
                        # loop
                        #print(f"Direction: {direction} and already visited: {positions[i][j]}")
                        loop = True
                        number_of_places += 1
                    else: 
                        #print(f"Adding {direction} to {i},{j}")
                        positions[i][j].append(direction)

            # restore the map
            map[o_i][o_j] = "X"

print(number_of_places)