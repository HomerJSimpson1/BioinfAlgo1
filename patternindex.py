def pat_index(pattern, genome):
    """
    Bioinformatics Algorithms 1 (2015) Coursera Class.  Interactive Text Code Challenge
    #4.
    The task is to find the indices of all occurences of the pattern (can be overlapping)
    that can be found in the string given by genome.  The indices here should be 
    zero-indexed.
    Input: Two strings, pattern and genome.
    Ouptut: A collection of space-separated integers specifying all starting positions
    where pattern appears as a substring of genome.
    """

    #count = 0
    #print(len(genome), len(pattern))
    indices = []

    for i in range(len(genome) - len(pattern)):
        #print(i)
        #print(genome[i:i + len(pattern)])
        if genome[i:i + len(pattern)] == pattern:
            indices.append(str(i))

    answer = ' '.join(indices)

    return answer
    
