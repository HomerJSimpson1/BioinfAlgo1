import hamming
#import patternindex
#import freqarray

def approx_pattern_count(pattern, text, d):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in Chapter 2, Section 2.4 ("Some Hidden Messages Are More Elusive Than Others").
    This is the approximate pattern matching problem.  Given a text, a pattern, and a 
    Hamming distance d, find all patterns within Hamming distance d of pattern in the text.
    Input: Strings pattern and text, as well as integer d (the Hamming distance).
    Output: All starting positions where pattern appears as a substring of text with at
    most d mismatches.
    """

    # Calculate all patterns within a Hamming Distance d from pattern.
    pats_to_search = gen_patterns_within_distance_d(pattern, d)

    # # Search for each of the above patterns in text
    # for pat in pats_to_search:
    #     patternindex.pat_index(pat, text)


    # Iterate through the text, and compare the current pattern to see if it is an element
    # of the pats_to_search.
    indxlist = []
    for i in range(len(text)):
        if text[i:i+len(pattern)] in pats_to_search:
            indxlist.append(i)

    return(indxlist)

def gen_patterns_within_distance_d(pattern, d):
    """
    This helper function is used to generate all patterns within a Hamming distance d
    of the pattern given by pattern.
    Input: A string, pattern, and an integer, d (the Hamming distance).
    Output: A list of all patterns within Hamming distance d of the given pattern.
    """

    alphabet = ['A', 'C', 'G', 'T']

    # patlist = [ pattern ]

    # for indx in range(len(pattern)):
    #     for nt in alphabet:
    #         newpat = pattern[:i] + nt + pattern[i+1:]
    #         patlist.append(newpat)

    allpatlist = gen_list_of_patterns(alphabet, len(pattern))
    patlist = []

    for val in allpatlist:
        hamdist = hamming.hamming(pattern, val)
        if hamdist <= d:
            patlist.append(val)

    #print(patlist)
    return(patlist)



def gen_list_of_patterns(alphabet, k):
    """
    Helper function used to generate all possible patterns of a size (given by k)
    using the alphabet (given by alphabet).
    """

    alphalen = len(alphabet)
    mylist = []
    temp = ''

    for i in range(alphalen**k):
        for j in range(k):
            temp += alphabet[int(i/(4**j)) % alphalen]
        mylist.append(temp)
        temp = ''

    return(mylist)
