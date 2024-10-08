with open('text.txt', 'r') as infile:
    spis = infile.readlines()

with open('output.txt', 'w') as outfile:
    for line in spis:
        outfile.write(line[::-1] + '\n')