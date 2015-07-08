def skew(genome):
    """
    Calculate the skew (#G - #C) at all positions of the genome.
    Find the point at which it is a minimum.  This is used to estimate the 
    oriC (origin of replication).
    Plot the graph of k vs skew(k).
    """

    klist = []
    gminusc = []
    numG = 0
    numC = 0

    #print(len(genome))

    for i in range(len(genome)):
        #print(i, genome[i])
        if genome[i] == 'G':
            numG += 1
            #print(numG)
        elif genome[i] == 'C':
            numC += 1
            #print(numC)
        klist.append(i)
        gminusc.append(numG - numC)

    # Find the index of the minimum value of G minus C.
    minval = min(gminusc)
    minindx = gminusc.index(minval)
    print(minindx, minval)
    #print(klist)

    # Some time in the future, should add capability to plot k vs gminusc.

    return(minindx)
