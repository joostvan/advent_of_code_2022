# how many overlapping pairs are there
# read_input
# array
# for line check min/max
# sum if so
def input():
    with open('inputday5.txt', 'r') as f:
        
    f.close()
    return assignment_pairs
def part1():
    pairs = 0
    data = input()
    for entry in data:
        first, second = entry.split(",")
        first= [int(i) for i in first.split('-')]
        second = [int(i) for i in second.split('-')]
        #
        if first[0] <= second[0] and first[1] >=second[1]:
            pairs += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            pairs +=1
        else:
            continue
    return pairs

def part2():
    pairs = 0
    data = input()
    for entry in data:
        first, second = entry.split(",")
        first= [int(i) for i in first.split('-')]
        second = [int(i) for i in second.split('-')]
        #
        if first[0] in range(second[0],second[1]+1) or first[1] in range(second[0],second[1]+1):
            pairs += 1
        elif second[0] in range(first[0],first[1]+1) or second[1] in range(first[0],first[1]+1):
            pairs +=1
        else:
            continue
    return pairs
res = part2()
print(res)