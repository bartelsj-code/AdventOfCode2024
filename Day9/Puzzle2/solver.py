
def convert_input():
    f = open("Day9\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = b.strip()
        output = d
    f.close()
    return output

def expand(input):
    #take compressed input and expand into full disk space
    #returns representation of disk as list
    disk = []

    i = 0
    block = True
    j = 0
    while i < len(input):
        length = int(input[i])
        if block:
            lst = [j]*length
            j += 1
        else:
            lst = [None]*length
        disk += lst
        block = not block
        i += 1
    return disk


def find_next_slot(index, size, disk):
    #given an index and a size, looks for and returns the index of the next gap in disk of that size. If not found, returns none
    i = index + 1
    while i < len(disk):
        j = 0
        while disk[i+j] == None:
            j += 1
            if j == size:
                return i
            if i+j >= len(disk):
                return None
        i = i+j + 1
    return None

def add_at_index(value, index, length, lst):
    #adds n = length characters of type value at position index in lst
    for i in range(index, index+length):
        lst[i] = value

def update_indicies(dct, length, disk):
    #goes through position dict and updates indicies
    for i in range(1, 10):
        if dct[i] != None:
            for j in range(dct[i], dct[i] + i):
                if disk[j] != None:
                    dct[i] = find_next_slot(dct[i], i, disk)
                    break

def main():
    #linear time (or really O(m*n) where m is the number of different file sizes but in this puzzle m = 9 is a constant)

    input = convert_input()
    print(len(input))
    disk = expand(input)

    #dict to track the next avaliable slot of a certain size
    slot_indicies = {}
    for i in range(1,10):
        slot_indicies[i] = find_next_slot(-1, i, disk)


    # go through list from back to front. using file id, get length of block, move the full block to the index stored for that block length in slot_indicies. update indicies and remove values from original positions
    i = len(disk)-1
    while i > slot_indicies[1]:
        id = disk[i]
        if id != None:
            block_length = int(input[id*2])
            if slot_indicies[block_length] != None and slot_indicies[block_length] < (i - block_length) + 1:
                add_at_index(id, slot_indicies[block_length], block_length, disk)
                add_at_index(None, (i-block_length)+1, block_length, disk)
                update_indicies(slot_indicies, block_length, disk)
            i -= int(block_length)
        else:
            i -= 1


    #get checksum
    total = 0
    i = 0
    while i < len(disk):
        if disk[i] != None:
            total += i*disk[i]
        i += 1

    print(total)

    

main()