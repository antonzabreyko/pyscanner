import re
class PyScanner():

    def __init__(self, string, separator=" "):
        self.string = string
        self.separator = separator


    def next(self):
        cond, index = self.hasNext(True)
        if (not cond):
            raise IndexError("index out of bounds")

        k = index

        g = len(self.string)

        for i in range(k, len(self.string)):
            if (self.string[i] == self.separator):
                g = i
                break

        partition = self.string[k:g]
        self.string = self.string[g:]
        return partition

    def hasNext(self, index=False):
        results = PyScanner.__hasNext__(self, "[^" + self.separator + "]")
        return index and results or results[0]

    def __hasNext__(self, param):
        match = re.search(param, self.string)
        if not match:
            return (False, -1)
        return (True, match.start())

    def hasNextInt(self):
        regex = "?[-][0-9]+"
        return self.__hasNext__(regex)
