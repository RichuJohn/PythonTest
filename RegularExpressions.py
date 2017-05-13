"""to learn how to deal with regular expressions in python"""

import re

def string_value_matcher():
    """matcher to get the count of how many times a regular expression matches
    but still the regular expression is the simplest of its kind
    """
    regex_pattern = r'wikipedia'
    test_string = "https://wikipedia.com/wikipedia"
    match = re.findall(regex_pattern, test_string)
    if __name__ == '__main__':
        print("Number of matches :", len(match))

string_value_matcher()
print(string_value_matcher.__doc__)


def read():
    """method to read from stdin"""
    raw_string = input() + ": read from stdin"
    if len(raw_string) >= 1 & len(raw_string) <= 500:
        return raw_string

STRING_AFTER_READING = read()
print(STRING_AFTER_READING)
