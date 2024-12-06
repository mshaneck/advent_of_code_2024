puzzle_input = None

list1 = []
list2 = []

safe_count = 0

def check_for_safe(levels):
    print(f"Checking {levels}", end='')
    if is_safe(levels):
        print("SAFE")
        return True 
    print()
    for i in range(len(levels)):
        modified_levels = levels[0:i] + levels[i+1:len(levels)]
        print(f"\tChecking {modified_levels}", end='')
        if is_safe(modified_levels):
            print("SAFE")
            return True
        print()
    print("UNSAFE")
    return False

def is_safe(levels):
    first = True 
    increasing = True
    prev = -1

    for level in levels:
        level = int(level)
        if first and prev == -1:
            prev = level
            continue
        
        if level == prev:
            print(f"*******************Diff is too small: {level} - {prev}")
            return False

        diff = level - prev 
        
        if abs(diff) > 3:
            print(f"*******************Diff is too big: {level} - {prev}")
            return False

        if first:
            # really second. need to establish increasing
            #print(f"Establishing increasing: {diff>0}")
            increasing = diff > 0
            first = False
            prev = level
            continue

        if increasing != (diff > 0): 
            #print("unsafe list")
            print(f"*******************Increasing changed: {increasing} {prev} {level}")
            return False
        prev = level
    return True
    
with open("./puzzle.input", "r") as f:
    for line in f:
        if check_for_safe(line.split()):
            safe_count += 1

print(safe_count)

            