in_file = open('input.txt', 'r')
print(in_file.readline())
out_file = open('output.txt', 'w')
for line in in_file:
    words = line.split()
    x, y = words
    out_file.write('%-8s  %-8s\n' % (x, y))
