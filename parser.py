from scanner_1 import *

args = sys.argv[1:]
# Iterating through args list and storing it into results
filename = ''
# args is a list of the command line args
# args stands for 'arguments'
for arg in args:
    filename += "" + arg

file = str(filename)
fhand = open(file, 'r')  # opens the file and reads it

def p_keywords():
    print("<<<<<Entering keywords>>>>>")

    for line in fhand:  # fhand allows us to handle the file
        word = line.split()  # line.split() reads each line in the file and splits the line into individual words
                              # and does not include spaces (small and large)
        word = line.strip()

    # use the array from scanner
    # assign the words in the keywords array to its appropriate token code
    for each_item in array_keywords:
        if word in keywords(filename):
            print("Next token is: 11 Next lexeme is", each_item)
    print("<<<<<Exiting keywords>>>>>")

def main():
    p_keywords()
main()

def p_identifiers():
    pass

def p_operators():
    pass
def p_special_characters():
    pass


def getNextToken(token):
    pass