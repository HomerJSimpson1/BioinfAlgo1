# Filename = fileio.py

def read_file_to_string(fname, nocrlf = True):
    """
    Read the contents of a file, specified by fname (full path), into a string.
    If nocrlf == True, then all returns will be removed from the string.
    Input: A string specifying the name of the file (full path).
    Output: A string representing the contents of the file.
    """

    if nocrlf:
        with open (fname, "r") as myfile:
            data=myfile.read().replace('\n', '')
    else:
        # Returns each line of the file as an element of a list.
        # The last character of each line is the return character ('\n')
        with open(fname, "r") as myfile:
            data=myfile.readlines()

    return data
