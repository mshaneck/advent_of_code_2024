puzzle_input = None

list1 = []
list2 = []

safe_count = 0

with open("./puzzle.input", "r") as f:
    for line in f:
        first = True 
        increasing = True
        prev = -1

        levels = line.split()
        safe = True
        error = "Safe"
        
        for level in levels:
            level = int(level)
            if first and prev == -1:
                prev = level
                continue
            
            if level == prev:
                error = f"*******************Diff is too small: {level} - {prev}"
                safe = False
                break

            diff = level - prev 
            
            if abs(diff) > 3:
                error = f"*******************Diff is too big: {level} - {prev}"
                safe = False
                break

            if first:
                # really second. need to establish increasing
                print(f"Establishing increasing: {diff>0}")
                increasing = diff > 0
                first = False
                prev = level
                continue


            if increasing != (diff > 0): 
                #print("unsafe list")
                error = f"*******************Increasing changed: {increasing} {prev} {level}"
                safe = False
                break
            prev = level
        
        print(f"{levels} is safe? {safe}: {error}")
        if safe:
            safe_count += 1


print(safe_count)

            