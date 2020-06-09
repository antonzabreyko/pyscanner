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
        while (self.string != ""):
            current = self.string[0]
            if current != self.separator:
                return True
            self.string = self.string[1:]
        return False
