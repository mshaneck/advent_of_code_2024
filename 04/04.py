f = open("puzzle.input", "r")
puzz = []
for line in f:
    puzz.append(line.rstrip())

height = len(puzz)
width = len(puzz[0])

# i is row
# j is column
# dir_i = -1,0,1 for up,none,down (up being lower numbers)
# dir_j = -1,0,1 for left, none, right
def search(i,j, dir_i, dir_j):
    # look for enough room
    if (dir_i == -1 and i < 3) or (dir_i == 1 and i > height-4) or \
        (dir_j == -1 and j < 3) or (dir_j == 1 and j > width-4):
        return 0
    target = "XMAS"
    for k,l in enumerate(target):
        if puzz[i+(dir_i*k)][j+(dir_j*k)] != l:
            return 0
    return 1
    
count = 0

for i,line in enumerate(puzz):
    for j,c in enumerate(line):
        # character c is at i,j
        if c == "X":
            count += search(i, j, -1, -1) # up left
            count += search(i, j, -1, 0)  # up
            count += search(i, j, -1, 1)  # up right
            count += search(i, j, 0, -1)  # left
            count += search(i, j, 0, 1)   # right
            count += search(i, j, 1, -1)  # down left
            count += search(i, j, 1, 0)   # down
            count += search(i, j, 1, 1)   # down right

print(count)