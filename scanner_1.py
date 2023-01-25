import sys

# Arrays created to store the operators, special characters, keywords, and constants.
array_keywords = ['integer', 'set', 'import', 'description', 'symbol', 'forward', 'return', 'type', 'parameters',
                      'of',
                      'array', 'type', 'specifications', 'enumerate', 'is', 'struct', 'variables', 'define', 'double',
                      'float', 'function', 'byte', 'input', 'array[]', 'do', 'while', 'if', 'endwhile', 'increment',
                      'endstruct',
                      'declarations', 'fshah', 'bslash', 'string', 'unsignicon', 'hcon', 'fcon', 'interface',
                      'structype',
                      'definetype', 'mextern', 'pointer of', 'mvoid', 'count', 'short', 'real', 'tbool', 'char',
                      'tstring of length signicon',
                      'tbyte', 'enum', 'global declarations', 'constants', 'persistent', 'shared', 'static', 'mfile',
                      'pointer',
                      'tunsigned', 'long', 'lb', 'value', 'equop', 'rb', 'comma', 'implementations', 'pbegin',
                      'precondition',
                      'not', 'rp', 'relop', 'mtrue', 'mfalse', 'equals', 'greatert', 'lesst', 'alters', 'preserves',
                      'produces',
                      'consumes', 'plus', 'minus', 'band', 'bor', 'bxor', 'star', 'divop', 'mod', 'lshift', 'rshift',
                      'address', 'deref', 'negate', 'letter',
                      'add', 'subtract', 'from', 'set', 'read', 'display', 'displayn', 'mclose', 'mfile', 'decrement',
                      'call',
                      'then', 'endif', 'for', 'repeat', 'until', 'endrepeat', 'while', 'mendcase', 'mbreak', 'mexit',
                      'endfun',
                      'downto', 'using', 'lp', 'mwhen', 'colon', 'default', 'dot', 'main']

array_op = [':=', '**', '+', '-', '*', '/', '<', '>', '<=', '>=', '=', '<>', '->']
array_special_char = [';', '.', '(', ')', '[', ']', '(* *)', '%', ',', '"="', '^', '_']
array_constants = ['A0', 'MAX', 'ARRAY_SIZE']

def op_and_specialchar(filename):
    operators_found = []
    spec_characters_found = []

    file = str(filename)
    fhand = open(file, 'r')  # opens the file and reads it


    for line in fhand:  # fhand allows us to handle the file
        words = line.split()  # line.split() reads each line in the file and splits the line into individual words
                              # and does not include spaces (small and large)
        words = line.strip()

        # i represents the item as 'for' traverses through each item in the array
        for i in array_op:
            # checks to see if each item in the array is found
            if i in words:
                operators_found.append(i)
        for i in array_special_char:
            # checks to see if each item in the array is found
            if i in words:
                spec_characters_found.append(i)
    print('Operators Found: ', operators_found)
    print('Special Characters Found: ', spec_characters_found)


def identifiers(filename, searchTerms):
    file = str(filename)
    fhand = open(file, 'r')

    # created an array to store any identifiers found
    identifiers_found = []

    # stored the terms we wanted to search into an array called searchThese[]
    # note: searchTerms[] comes from the identifier_keywords in the main as a parameter
    searchThese = []
    for i in range(len(searchTerms)):
        searchThese = searchTerms[i]

    for line in fhand:
        words_in_line = line.split()
        # if identifier_keywords are in words_in_line then...
        if searchThese in words_in_line:
            # store the index where the identifier keyword is to keep track of it
            i = words_in_line.index(searchThese)
            # append the word next to the keyword
            identifiers_found.append(words_in_line[i+1])
    print('Identifiers_Found : ', identifiers_found)

def constants(filename):
    constants_found = []
    file = str(filename)
    fhand = open(file, 'r')

    for line in fhand:
        words = line.split() # line.split() reads each line in the file and splits the line into individual words
        # and does not include spaces (small and large)
        for i in array_constants:
            if i in words:
                constants_found.append(i)
    # *set gets rid of duplicates in the array constants_found and stores them in res for 'result'
    res = [*set(constants_found)]
    print('Constant Found: ', res)

    # We weren't sure how to iterate to the next lines after the word
    # 'constants'
    # with open(file, 'r') as f:
    #     for line in f:
    #         if line.startswith("constants"):
    #             next_line = next(f)
    #             line1 = line
    #             line2 = next(f)
    #             print(line2)
    #             f.close


def keywords(filename):
    keywords_found = []
    file = str(filename)
    fhand = open(file, 'r')

    for line in fhand:
        words = line.split()  # line.split() reads each line in the file and splits the line into individual words
        # and does not include spaces (small and large)
        words = line.strip()

        for i in array_keywords:
            # checks to see if each item in the array is found
            if i in words:
                keywords_found.append(i)

    #print('Keywords Found: ', keywords_found)
    return keywords_found



# main method
# if __name__ == '__main__':
def scanner():
    # args is a list of the command line args
    # args stands for 'arguments'
    args = sys.argv[1:]

    # Iterating through args list and storing it into results
    result = ''
    for arg in args:
        result += "" + arg

    # created a list of words that we want to search for before the identifiers are found
    identifier_keywords = ['function', 'interface', 'struct', 'structype', 'function', 'mclose', 'mfile', 'to', 'from', 'symbol', 'define']
    constants_keywords = ['constants']

    op_and_specialchar(result)
    keywords(result)
    temp = []
    for each_item in identifier_keywords:
        temp.append(each_item)
    identifiers(result, temp)
    constants(result)
# scanner()