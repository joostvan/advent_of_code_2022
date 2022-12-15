# find where two strings overlap and add sum
import logging
def get_input():
    file = open("inputday3.txt","r")
    input = []
    for line in file.readlines():
        input.extend(line.strip().split("\n"))
    return input

def score(c):
    if 'a' <=c<='z':
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A')+1 + 26

def main():
    data = get_input()
    # #print(input)
    # res = set()
    # for line in input:
    #     #len = 0
    #     length = len(line)//2
    #     #print(len)
    #     #print(line, len)
    #     #print(len)
    #     s1 = line[int(0):int(length)]
    #     s2 = line[int(length):]
    #     for i in s1:
    #         if i in s2 and not i in res:
    #             res.update(i)
    # sum = 0
    # print(res)
    # for entry in res:
    #     try:
    #         sum+=score(entry)
    #         #print(sum)
    #     except:
    #         logging.debug("Error on sum")
    # print(sum)
    # return sum
    # Instanciate mappings between item letter and associated priority
    letter2prority = {
        **{chr(i): p + 1 for p, i in enumerate(range(ord("a"), ord("z") + 1))},
        **{chr(i): p + 27 for p, i in enumerate(range(ord("A"), ord("Z") + 1))},
    }

    # Part 1: Find the common items between the 2 compartments for each rucksack.
    # What is the sum of the priorities of those items?
    priority_sum = 0
    for rucksack in data:
        n = len(rucksack)
        first_compartiment_items = set(rucksack[: n // 2])
        second_compartiment_items = set(rucksack[n // 2 :])

        # Filter items present in both compartments
        duplicated_items = first_compartiment_items.intersection(
            second_compartiment_items
        )

        # Sum of priorities
        for item in duplicated_items:
            priority_sum += letter2prority.get(item, 0)

    #print(priority_sum)
    priority_sum = 0
    for group_id in range(len(data) // 3):
        first_rucksack = set(data[group_id * 3])
        second_rucksack = set(data[group_id * 3 + 1])
        third_rucksack = set(data[group_id * 3 + 2])

        duplicated_item = first_rucksack.intersection(second_rucksack).intersection(
            third_rucksack
        )
        assert (
            len(duplicated_item) == 1
        ), "There is more than 1 common item within the group"

        priority_sum += letter2prority[list(duplicated_item)[0]]
    print(priority_sum)
main()