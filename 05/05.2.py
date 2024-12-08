f = open("puzzle.input", "r")
rules = {}

def is_valid(pages):
    global rules
    valid = True
    for i,page in enumerate(pages):
        if page in rules:
            for seconds in rules[page]:
                if seconds in pages[0:i]:
                    # rule is violated
                    valid = False
    return valid

def sort_pages(new_pages, pages):
    if not is_valid(new_pages):
        return None
    if len(pages) == 0:
        return new_pages
    page_to_insert = pages.pop()
    if len(new_pages) == 0:
        return sort_pages([page_to_insert], pages)
    for i in range(len(new_pages)+1):
        new_copy = new_pages[0:i] + [page_to_insert] + new_pages[i:]
        new_copy = sort_pages(new_copy, pages)
        if new_copy is not None:
            return new_copy
    return None        

correct_sum = 0
fixed_sum = 0

for line in f:
    if "|" in line:
        (first, second) = line.rstrip().split("|")
        if first not in rules:
            rules[first] = []
        rules[first].append(second)

    if "," in line:
        pages = line.rstrip().split(",")
        
        if not is_valid(pages):
            print(f"Not valid: {pages}")
            # Fix it
            l = len(pages)
            pages = sort_pages([], pages)
            if pages is None:
                print("SOMETHING IS SCREWWED UP")
            else:
                print(f"Fixed to {pages}")
                fixed_sum += int(pages[(len(pages)-1)//2])
        else:
            correct_sum +=  int(pages[(len(pages)-1)//2])

print(f"fixed: {fixed_sum}")
print(f"correct sum: {correct_sum}")
