# Filename: freqarray.py

DNA_ALPHABET = ['A', 'B', 'C', 'D']

def gen_freq_array(alphabet, k):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    in the charging station topic, "The Frequency Array."
    Input: The alphabet of symbols to use and the length k of each k-mer.
    Output: A frequency array initialized to each possible k-mer with a frequency of 0.
    """

    # There are (len(alphabet))^k - 1 possible k-mers.
    #left = [ [alphabet[i]] * len(alphabet)**k/len(alphabet) for i in range(len(alphabet)) ]
    left = [ [alphabet[i]] * ((len(alphabet))**(k-1)) for i in range(len(alphabet)) ]
    left1 = sum(left, [])

    # Have to figure out how to get the middle values, and when I don't know how long
    # the alphabet is.

    alphalen = len(alphabet)
    #print(alphalen, k)
    #print(alphalen**k)

    right = alphabet * (alphalen**(k-1))

    mylist = []
    temp = ''
    #for i in range(alphalen**(k-1)):
    for i in range(alphalen**k):
        for j in range(k):
            temp += alphabet[int(i/(4**j)) % alphalen]
        mylist.append(temp)
        temp = ''

    #print(mylist)

    mydict = { mylist[i]:0 for i in range(len(mylist)) }

    print(mydict)
    return(mydict)
