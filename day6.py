def input():
    with open('inputday6.txt', "r") as f:
        line = f.readline()
    f.close()
    return line

def parta():
    line = input()
    for i in range(len(line)):
        if len(set(line[i:i+4]))==4:
            print(i+4)
            break
            
def partb():
    line = input()
    for i in range(len(line)):
        if len(set(line[i:i+14]))==14:
            print(i+14)
            break
partb()