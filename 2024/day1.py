def part1():
    print("ADVENT OF CODE - DAY 1 - PART 1")
    list1 = []
    list2 = []
    with open('puzzle.txt', 'r') as file:
        for line in file:
            values = line.strip().split() 
            list1.append(int(values[0]))
            list2.append(int(values[1]))

    if len(list1) != len(list2):
        print("YO - WTF!")
    else:
        list1 = sorted(list1)
        list2 = sorted(list2)
        total_diff=0
        for index in range(len(list1)):
            #print(abs(list1[index] - list2[index]))
            total_diff += abs(list1[index] - list2[index]) 
    print(total_diff)

def part2():
    print("ADVENT OF CODE - DAY 1 - PART 2")
    list1 = []
    list2 = []
    with open('puzzle.txt', 'r') as file:
        for line in file:
            values = line.strip().split() 
            list1.append(int(values[0]))
            list2.append(int(values[1]))

    if len(list1) != len(list2):
        print("YO - WTF!")
    else:
        total_diff=0
        for index in range(len(list1)): 
            mult = list2.count(list1[index])
            total_diff += list1[index] * mult
              
    print(total_diff)


def main():
    part1()
    part2()
    
if __name__ == "__main__":
    main()
