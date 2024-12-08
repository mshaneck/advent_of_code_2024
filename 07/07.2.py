f = open("puzzle.input", "r")

def check(target, num_list, current_value, operations, indent):
    if len(num_list) == 0:
        #print("\t"*indent + f"End of the list: {target} {current_value} {operations}")
        #if current_value == target:
            #print("\t"*indent + f"Got it: {target} operations {operations}")
        return current_value == target
    next_num = num_list.pop(0)
    #print("\t"*indent + f"Target: {target}, Current value: {current_value}, num_list = {next_num},{num_list}, operations {operations}")
    if current_value == -1:
        current_value = next_num
        return check(target, num_list, current_value, [], indent+1)
    else:
        # Try multiplication
        current_val_mult = current_value * next_num
        #print("\t"*indent + "Trying mult")
        # Only recurse if it is not too big already
        if current_val_mult <= target:
            if check(target, list(num_list), current_val_mult, list(operations+["*"]), indent+1):
                return True 
        #print("\t"*indent + "Trying add")
        
        # Try add
        current_val_add = current_value + next_num
        if current_val_add <= target:
            if check(target, list(num_list), current_val_add, list(operations+["+"]), indent+1):
                return True
        
        # Try concatenation
        current_val_cat = int(str(current_value) + str(next_num))
        if current_val_cat <= target:
            if check(target, list(num_list), current_val_cat, list(operations+["||"]), indent+1):
                return True 
            
    return False
        
count = 0
for line in f:
    target,nums = line.rstrip().split(":")
    num_list = nums.strip().split()

    target = int(target)
    num_list = [int(x) for x in num_list]
    #print("-"*80)
    #print(line)
    if check(target, list(num_list), -1, [], 0):
        count += target

print(count)
    
