def hamming(string1, string2):
    """
    Find the Hamming distance between two strings.
    Input: The two strings to be compared.
    Output: The Hamming distance between the two strings.
    """

    strlen1 = len(string1)
    strlen2 = len(string2)

    if strlen2 < strlen1:
        strlength = strlen2
    else:
        strlength = strlen1

    hamcount = 0
    for i in range(strlength):
        if string1[i] != string2[i]:
            hamcount += 1

    return(hamcount)
        
