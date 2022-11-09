max_chars = int(input('Enter max amount of acceptable characters: '))
fname = input('Enter file to check: ')

strip_lines = 'x'
while not strip_lines == 'y' and not strip_lines == 'n':
    strip_lines = input('Strip whitespace when checking lines? (y/n) ')

f = open(fname, "r")
lines = f.readlines()

count = 0
for line in lines:
    curr_line = line
    if strip_lines == 'y':
        curr_line = line.strip()
    count += 1
    if (len(curr_line) > max_chars):
        print('Line ' + str(count) + ' is more than ' + str(max_chars) + ' characters long')
        print('Line contents are: ' + curr_line + '\n')