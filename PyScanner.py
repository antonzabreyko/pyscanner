import re
''' Scanner object for strings. Based on Java's scanners. '''
class PyScanner():

    ''' Initialization method. Takes in the string to be scanned, and an
        optional separator character. By default the separator is whitespace. '''
    def __init__(self, string, separator=" "):
        self.string = string
        self.separator = "[^" + separator + "]+"


    def __next__(self, param):
        cond, start, end = self.__hasNext__(param)
        if (not cond):
            raise IndexError("index out of bounds")

        partition = self.string[start:end]
        self.string = self.string[end:]
        return partition


    ''' Returns the next partition of the string, closed off by the separator. '''
    def next(self):
        return self.__next__(self.separator)

    def hasNext(self, index=False):
        results = PyScanner.__hasNext__(self, self.separator)
        return index and results or results[0]

    def __hasNext__(self, param):
        match = re.search(param, self.string)
        if not match:
            return (False, -1, -1)
        return (True, match.start(), match.end())

    def hasNextInt(self):
        regex = "[-]?[0-9]+"
        return self.__hasNext__(regex)[0]

    def nextInt(self):
        regex = regex = "[-]?[0-9]+"
