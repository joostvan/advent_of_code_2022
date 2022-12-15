# how many overlapping pairs are there
# read_input
# array
# for line check min/max
# sum if so
def input():
    with open('inputday4.txt', 'r') as f:
        lines = f.readlines()
        assignment_pairs = [entry.strip() for entry in lines]
    return assignment_pairs
def rng(a,b):
    a_s, a_f = map(int, a.split('-'))
    a_b, b_f = map(int, b.split('-'))
    return a_b <= a_s and a_f <= b_f
    

def main():
    text = input()
    print(text)
main()