

def convert_input():
    f = open("Day25\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()
    objs = []
    curr = []
    for line in lines:

        if line == "":
            objs.append(curr)
            curr = []
            continue

        curr.append(list(line))
    objs.append(curr)

    for curr in objs:
        for row in curr:
            for i in range(len(row)):
                row[i] = 1 if (row[i] == "#") else 0

    keys = []
    locks = []
    for curr in objs:
        #rotate list and get sums
        rot  = list(zip(*curr[::-1]))  #  <-- not my own code
        if rot[0][0] == 1:
            keys.append([sum(row)-1 for row in rot])
        else:
            locks.append([sum(row)-1 for row in rot])
    return keys, locks

def fits_lock(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

def main():
    keys, locks = convert_input()

    count = 0
    for key in keys:
        for lock in locks:
            if fits_lock(key, lock):
                count += 1
    print(count)
main()


