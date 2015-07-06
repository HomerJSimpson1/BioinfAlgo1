
#import math

def patterncount(text, pattern):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    #1, in the first chapter, first section.
    The task is to count the number of occurences of the pattern (can be overlapping)
    that can be found in the string given by text.
    """
    count = 0
    #print(len(text), len(pattern))

    for i in range(len(text) - len(pattern)):
        #print(i)
        #print(text[i:i + len(pattern)])
        if text[i:i + len(pattern)] == pattern:
            count += 1

    return count


def frequent_words(text, k):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    #2, in the first chapter, first section.
    Given a string text and a length k, find the most frequently occuring patterns of
    length k in the string text.
    """
    freq_patterns = []
    patterns = {}

    for i in range(len(text) - k):
        pattern = text[i:i + k]
        count = patterncount(text, pattern)
        #patterns[count] = pattern #Can't do this, because could create duplicate keys
        if pattern not in patterns:
            patterns[pattern] = count

    max_val = max(patterns.values())

    freq_patterns = [ pat for pat in patterns.keys() if patterns[pat] == max_val ]

    return freq_patterns
        

    
    
