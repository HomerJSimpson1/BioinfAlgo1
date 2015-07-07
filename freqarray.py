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
    
    return(myfreqdict)
