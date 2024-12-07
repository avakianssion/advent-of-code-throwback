def check_increasing(level):
    return level == sorted(level)

def check_decreasing(level):
    return level == sorted(level,reverse=True)

def check_safe(level):
    print(level)
    if check_increasing(level) or check_decreasing(level):
        for reading in range (len(level)-1):
            diff = abs(level[reading] - level[reading+1])
            if not 1<=diff<=3:             
                print("unsafe")
                return False
    else:
        print("unsafe - order")
        return False
    return True


def part1():
    '''
    check if we are increasing or decreasing - 
    - sort the list - reverse should be same as sorted
    - check if levels are not jumping by more than 3 
    '''
    print("ADVENT OF CODE - DAY 2 - PART 1")
    
    levels = []
    unsafe=0
    with open('puzzle.txt', 'r') as file:
        for line in file:
            levels.append([int (x) for x in line.split()])
    for level in levels:
        print(level)
        if check_increasing(level) or check_decreasing(level):
            for reading in range (len(level)-1):
                diff = abs(level[reading] - level[reading+1])
                if not 1<=diff<=3:             
                    print("unsafe")
                    unsafe+=1
                    break
        else:
            print("unsafe - order")
            unsafe+=1
    
    print (unsafe)

def part2():
    print("ADVENT OF CODE - DAY 2 - PART 2")
    
    levels = []
    safe=0
    with open('puzzle.txt', 'r') as file:
        for line in file:
            levels.append([int (x) for x in line.split()])
    for level in levels:
        if check_safe(level):
            print(level,"safe")
            safe+=1
        else:
            temp_level = level.copy()
            
            for i in range(len(level)):
                temp = level.copy()
                del temp[i]
                if check_safe(temp):
                    print(temp,"safe")
                    safe+=1
                    break
    print (safe)

def main():
    part1()  
    part2()
if __name__ == "__main__":
    main()
