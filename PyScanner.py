class PyScanner():

    def __init__(self, string, separator=" "):
        self.string = string
        self.separator = separator


    def next(self):
        k = None
        for i in range(len(self.string)):
            if self.string[i] != self.separator:
                k = i
                break

        if self.string == "" and k == None:
            raise IndexError("index out of bounds")

        g = len(self.string)

        for i in range(k, len(self.string)):
            if (self.string[i] == self.separator):
                g = i
                break

        partition = self.string[k:g]
        self.string = self.string[g:]
        return partition

    def hasNext(self):
        while (self.string != ""):
            current = self.string[0]
            if current != self.separator:
                return True
            self.string = self.string[1:]
        return False
