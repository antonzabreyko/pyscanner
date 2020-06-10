import re
class PyScanner():

    def __init__(self, string, separator=" "):
        self.string = string
        self.separator = separator


    def next(self):
        if (not self.hasNext()):
            raise IndexError("index out of bounds")

        g = len(self.string)

        for i in range(len(self.string)):
            if (self.string[i] == self.separator):
                g = i
                break

        partition = self.string[:g]
        self.string = self.string[g:]
        return partition

    def hasNext(self):
        return PyScanner.__hasNext__(self, "[^" + self.separator + "]")

    def __hasNext__(self, param):
        match = re.search(param, self.string)
        if not match:
            return False
        self.string = self.string[match.span()[0]:]
        return True

    def hasNextInt(self):
        return
