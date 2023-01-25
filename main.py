import sys
import re

def scanner(filename):
    # Arrays created to store the operators, special characters, keywords, and constants.
    array_op = [':=', '**', '+', '-', '*', '/', '<', '>', '<=', '>=', '=', '<>', '->']
    array_special_char = [';', '.', '(', ')', '[', ']', '(* *)', '%', ',', '"="', '^', '_']

    # nonterminals
    array_keywords = ['integer', 'set', 'import', 'description', 'symbol', 'forward', 'return', 'type', 'parameters', 'of',
                      'array', 'type', 'specifications', 'enumerate', 'is', 'struct', 'variables', 'define', 'double',
                      'float', 'function', 'byte', 'input', 'array[]', 'do', 'while', 'if', 'endwhile', 'increment', 'endstruct',
                      'declarations', 'fshah', 'bslash', 'string', 'unsignicon', 'hcon', 'fcon', 'interface', 'structype',
                      'definetype', 'mextern', 'pointer of', 'mvoid', 'count', 'short', 'real', 'tbool', 'char', 'tstring of length signicon',
                      'tbyte', 'enum', 'global declarations', 'constants', 'persistent', 'shared', 'static', 'mfile', 'pointer',
                      'tunsigned', 'long', 'lb', 'value', 'equop', 'rb', 'comma', 'implementations', 'pbegin', 'precondition',
                      'not', 'rp', 'relop', 'mtrue', 'mfalse', 'equals', 'greatert', 'lesst', 'alters', 'preserves', 'produces',
                      'consumes', 'plus', 'minus', 'band', 'bor', 'bxor', 'star', 'divop', 'mod', 'lshift', 'rshift', 'address', 'deref', 'negate', 'letter',
                      'add', 'subtract', 'from', 'set', 'read', 'display', 'displayn', 'mclose', 'mfile', 'decrement','call',
                      'then', 'endif', 'for', 'repeat', 'until', 'endrepeat', 'while', 'mendcase', 'mbreak', 'mexit', 'endfun',
                      'downto', 'using', 'lp', 'mwhen', 'colon', 'default', 'dot', 'main']

    operators_found = []
    spec_characters_found = []
    keywords_found = []
    constants_found = []
    identifiers_found = []

    # integers ________ --> identifier
    # constants _______ --> constants

    skip = False

    file = str(filename)
   # file = input("Enter the file name: ")  # asks user for text file
    fhand = open(file, 'r')  # opens the file and reads it
    for line in fhand:  # fhand allows us to handle the file
        words = line.split()  # line.split() reads each line in the file and splits the line into individual words
                              # and does not include spaces (small and large)

        # store words into a string called 'temp_string' and used re.finadall() to find the strings only
        # inside the quotation marks
        temp_string = str(words)
        quotation_string = re.findall('"([^"]*)"', temp_string)
        print(quotation_string)
        # x = str(quotation_string)
        # re.sub(x, ' "" ', quotation_string,
        #              flags=re.IGNORECASE)

        # i represents the item as 'for' traverses through each item in the array
        for i in array_op:
            # checks to see if each item in the array is found
            if i in words:
                operators_found.append(i)
        for i in array_special_char:
            # checks to see if each item in the array is found
            if i in words:
                spec_characters_found.append(i)
        for i in array_keywords:
            # checks to see if each item in the array is found
            if i in words:
                keywords_found.append(i)
    print('Operators Found: ', operators_found)
    print('Special Characters Found: ', spec_characters_found)
    print('Keywords Found: ', keywords_found)


# main method
if __name__ == '__main__':
    # args is a list of the command line args
    # args stands for 'arguments'
    args = sys.argv[1:]

    # Iterating through args list and storing it into results
    result = ''
    for arg in args:
        result += "" + arg

    scanner(result)

#include identifiers