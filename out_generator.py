from itertools import permutations

arr = []

def read_file():
    file1 = open('100000_random_5k.txt', 'r')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = file1.readline()

        # end of file
        if not line:
            break
        arr.append(int(line.strip()))

    file1.close()

def write_file():
    out_file = open("100.txt", "w")

    # write line to output file
    for i in range(100000):
        num = 1
        out_file.write('%d' % num)
        out_file.write("\n")

    out_file.close()


l = list(permutations(range(1, 7)))
print(l)