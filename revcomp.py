def rev_comp(pattern):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    #3.
    Input: A DNA string pattern
    Output: The reverse complement of pattern.
    """
    # A dictionary to use to look up the complement of a given nucleotide.
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

    revcomplist = [ comp[pattern[i]] for i in range(-1, -(len(pattern) + 1), -1) ]
    revcomp = ''.join(revcomplist)
    
    # Nevermind, the following was starting to get complicated....
    # Use a list of symbols, set up so that adding 2 to the index of any given
    # index, mod 4, will yield its complement.
    # The index for 'A' is 0 and the index for 'T' is 2.
    # e.g. adding 2 + 2 = 4 mod 4 = 0. 
    #comp = ['A', 'C', 'T', 'G']
    
    return revcomp
