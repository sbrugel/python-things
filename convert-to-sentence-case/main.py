fname = input('Enter file to check: ')

f = open(fname, "r")
lines = f.readlines()

count = 0
for line in lines:
    count += 1
    capsFlag = True 
    newstr = ''
    for i in range(len(line)):
        if not line[i].isalpha(): # this character is not a letter
            newstr += line[i] # keep character as it is
            if line[i] == '.': # capitalize first letter of next sentence
                capsFlag = True
        else:
            if capsFlag: # should this line be capitalized? (True if it should be)
                capsFlag = False # stop capitalizing until the next sentence
                if line[i].lower() == line[i]: # this character is lowercase, so capitalize it
                    newstr += line[i].upper()
                else:
                    newstr += line[i]
            else:
                if line[i].upper() == line[i]: # this character is capital, so lowercase it
                    newstr += line[i].lower()
                else:
                    newstr += line[i]
    print(newstr)