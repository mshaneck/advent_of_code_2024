f = open("puzzle.input", "r")
puzz = []
for line in f:
    puzz.append(line.rstrip())

height = len(puzz)
width = len(puzz[0])

# i is row
# j is column
def search(i,j):
    # check for space
    if i == 0 or j == 0 or i == height-1 or j == width-1:
        return False
    
    # check cross
    if (puzz[i-1][j-1] == "S" and puzz[i+1][j+1] == "M") or (puzz[i-1][j-1] == "M" and puzz[i+1][j+1] == "S"):
        if (puzz[i+1][j-1] == "S" and puzz[i-1][j+1] == "M") or (puzz[i+1][j-1] == "M" and puzz[i-1][j+1] == "S"):
            print("__________XXXX__________")
            print(puzz[i-1][j-1:j+2])
            print(puzz[i][j-1:j+2])
            print(puzz[i+1][j-1:j+2])
            return 1

    return 0
    
count = 0

for i,line in enumerate(puzz):
    for j,c in enumerate(line):
        # character c is at i,j
        if c == "A":
            count += search(i, j)

print(count)