# Filename: freqarray.py

DNA_ALPHABET = ['A', 'B', 'C', 'D']

def gen_freq_array(alphabet, k):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The alphabet of symbols to use and the length k of each k-mer.
    Output: A frequency array initialized to each possible k-mer with a frequency of 0.
    """

    # # There are (len(alphabet))^k - 1 possible k-mers.
    # #left = [ [alphabet[i]] * len(alphabet)**k/len(alphabet) for i in range(len(alphabet)) ]
    # left = [ [alphabet[i]] * ((len(alphabet))**(k-1)) for i in range(len(alphabet)) ]
    # left1 = sum(left, [])

    # # Have to figure out how to get the middle values, and when I don't know how long
    # # the alphabet is.

    # right = alphabet * (alphalen**(k-1))

    alphalen = len(alphabet)
    #print(alphalen, k)
    #print(alphalen**k)

    mylist = []
    temp = ''
    #for i in range(alphalen**(k-1)):
    for i in range(alphalen**k):
        for j in range(k):
            temp += alphabet[int(i/(4**j)) % alphalen]
        mylist.append(temp)
        temp = ''

    #print(mylist)
    mylist.sort()

    #mydict = { mylist[i]:0 for i in range(len(mylist)) }
    mydict = { mylist[i]:(i,0) for i in range(len(mylist)) }

    #print(mydict)
    return(mydict)



def get_freq_indx(freq_array, kmer):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The frequency array and the kmer for which we wish to retrieve the index.
    Output: The index of the kmer from the frequency array.  Returns -1 if the kmer is not
    found in the frequency array (actually implemented as a dictionary).
    """

    indx = -1

    if kmer in freq_array:
        indx = freq_array[kmer][0]
    else:
        print("Error: That kmer is not in the frequency array.")

    return indx


def get_kmer_from_index(freq_array, kmer_index):
    #if kmer_index in freq_array.values()[0]:
    #    kmer = freq_array.values()[kmer_index]

    kvpair = [ (k, v) for k, v in freq_array.items() if v[0] == kmer_index ]
    #print(kvpair)

    if len(kvpair) == 0:
        print("Error: That value was not found in the frequency array.")
        result = ''
    elif len(kvpair) == 1:
        #result = kvpair[0][1][0]
        result = kvpair[0][0]
    else:
        print("Error: That index was not unique.")
        result = ''

    return result


def get_frequency(freq_array, kmer):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The frequency array and the kmer for which we wish to retrieve the index.
    Output: The frequency with which the supplied kmer occurs in the genome.  Returns -1 
    if the kmer is not found in the frequency array (actually implemented as a dictionary).
    """

    freq_value = -1

    if kmer in freq_array:
        freq_value = freq_array[kmer][1]
    else:
        print("Error: That kmer is not in the frequency array.")

    return freq_value


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



def find_frequencies(genome, freq_array, k):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The genome to search, the frequency array with the frequency of each 
    possible k-mer initialized to 0, and the kmer length k.
    Output: A frequency array containing each possible k-mer and the frequency with which
    the k-mer is found in the given genome.
    """
    # for kmer in freq_array.keys():
    #     # Find the frequency of that kmer in the genome
    #     freq_count = patterncount(genome, kmer)
    #     freq_array[kmer][1] = freq_count

    for i in range(len(genome) - (k - 1)):
        kmer = genome[i:(i + k)]
        #freq_array[kmer][1] += 1 #Illegal in python
        freq_array[kmer] = (freq_array[kmer][0], freq_array[kmer][1] + 1)

    #print(freq_array)
    


def freq_array(genome, alphabet, k):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The genome to search, the alphabet of symbols to use and the length k of each k-mer.
    Output: A frequency array containing each possible k-mer and the frequency with which
    the k-mer is found in the given genome.
    """

    myfreqdict = gen_freq_array(alphabet, k)    

    #print(myfreqdict.values()["AAT"])

    # print(get_freq_indx(myfreqdict, "AAT"))
    # result = get_kmer_from_index(myfreqdict, 48)
    # print(result)

    # result = get_kmer_from_index(myfreqdict, 11)
    # print(result)

    find_frequencies(genome, myfreqdict, k)
    #print(myfreqdict)

    print_freq_array(myfreqdict)
    
    return(myfreqdict)


def print_freq_array(myfreqdict):
    """
    Helper function to print the frequencies in order of the index.
    Input: myfreqdict, a dictionary that represents a "frequency array."
    Output: Returns nothing, but prints the frequencies associated with each possible k-mer, in
    the order of the k-mer's index in the frequency array.
    """
    # for val in myfreqdict:
    #     print(myfreqdict[val].[1])

    freqlist = [ myfreqdict[val] for val in myfreqdict ]
    freqlist.sort()

    for val in freqlist:
        print(val[1])



def convert_pattern_to_number(pattern):
    """
    DNA String pattern converter that uses the idea that it is the same as converting
    from base 4 to base 10, and treating 'A'=0, 'C'=1, 'G'=2, 'T'=3.
    Input: Pattern, a pattern of DNA symbols.
    Output: The index of the pattern in the lexicographically-ordered frequency array.
    """

    alphadict = {'A':0, 'C':1, 'G':2, 'T':3}

    patlist = [ alphadict[symbol] for symbol in pattern ]
    
    j = 0
    num = 0

    for i in range(-1, -(len(patlist) + 1), -1):
        # Go through each digit, in reverse order (i.e. starting from the right and going
        # left), and multiply each successive digit by an increasing power of 4 (which is
        # the size of the alphabet).
        num += 4**j * patlist[i]
        #print(patlist[i], j, num)
        j += 1

    return(num)
        

def convert_number_to_pattern(num, k):
    """
    Converts a number to a pattern.  Successively divide num by 4 and get each remainder.
    The remainder (i.e. mod 4) yields each successive symbol in pattern, starting from
    the right side of pattern.
    This process is equivalent to converting from base 10 to base 4, and then using the
    symbols in alphadict to convert from numbers to digits.
    Input: num, a number to convert into a DNA String pattern, and k, the length of the string.
    Output: The pattern represented by num.
    """
    numalphadict = {0:'A', 1:'C', 2:'G', 3:'T'}

    #quotient = len(str(num))
    quotient = num / 4
    remainderlist = []

    while (num > 0):
        #quotient = num / 4
        remainder = num % 4
        #print(quotient, remainder)
        remainderlist.append(remainder)
        quotient = num / 4
        num = int(quotient)

    #print(len(remainderlist), k)

    #while (len(remainderlist) <= k):
    while (len(remainderlist) < k):
        #print("Appending A's")
        remainderlist.append(0)

    remainlist = [ str(numalphadict[item]) for item in remainderlist ]
    remainlist.reverse()
    pattern = ''.join(remainlist)

    return(pattern)

    
