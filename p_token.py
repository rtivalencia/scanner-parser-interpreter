import re
from scanner_1 import *

lexicalAnalyzer = {
    "keywords": {
        'array': 11,
        'begin': 11,
        'constant': 11,
        'declarations': 11,
        'display': 11,
        'do': 11,
        'else': 11,
        'endfun': 11,
        'endif': 11,
        'endrepeat': 11,
        'endwhile': 11,
        'enum': 11,
        'forward': 11,
        'function': 11,
        'global': 11,
        'if': 11,
        'implementations': 11,
        'integer': 11,
        'main': 11,
        'parameters': 11,
        'pointer': 11,
        'references': 11,
        'repeat': 11,
        'return': 11,
        'set': 11,
        'specifications': 11,
        'struct': 11,
        'symbol': 11,
        'then': 11,
        'type': 11,
        'until': 11,
        'while': 11
    },

    "arithOps": {
        '+': 6000,
        '-': 6001,
        '*': 6002,
        '\\': 6003,
        '>': 6004,
        '<': 6005,
        '>=': 6006,
        '<=': 6007,
        '==': 6008,
        '~=': 6009,
        '=': 6010
    },

    "tokens": {
        '\\(': 4000,  # open parenthesis
        '\\)': 4001,  # close parenthesis
        '\"': 4002,  # double quote
        '\[([a-zA-Z]|([\-]?[0-9]?.[0-9]))+\]': 4003,  # brackets containing words/numbers
        '[\-]?[0-9]': 4004,  # all numbers, including negative numbers
        '\/\*': 4005,  # Beginning of block comment
        '\*\/': 4006,  # End of block comment
        '\/\/': 4007,  # line comment
        '\[\]': 4008,  # empty brackets
        '\,': 4009,  # comma
        '\s+': 4010,  # whitespace
        '[a-zA-Z]+': 4011  # alpha word

    }

}


# Method to turn a word from the file into a Token.
def tokenize(word):
    numericalValue = 0

    # Test to see if word is a keyword.
    if word in lexicalAnalyzer["keywords"]:
        newToken = Token(word, "keyword", lexicalAnalyzer["keywords"][word])
        return newToken

    # Test to see if word is an arithmetic operator
    if word in lexicalAnalyzer["arithOps"]:
        newToken = Token(word, "arithmetic operator", lexicalAnalyzer["arithOps"][word])
        return newToken

    '''
    Test to see if the word is a token. Cycle through
    the keys of the "tokens" dictionary, using the keys as
    regular expressions tests. If there is a match, grab
    the value.
    '''
    for subkey in lexicalAnalyzer["tokens"].keys():
        if re.match(subkey, word):
            numericalValue = lexicalAnalyzer["tokens"][subkey]

    # If numericalValue is 0, then it has fallen through all the tests,
    # which means it was not matched with anything.
    if numericalValue == 0:
        return "No match found."
    newToken = Token(word, "token", numericalValue)
    return newToken