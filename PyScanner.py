class PyScanner():

    def __init__(self, string, separator=" "):
        self.string = string
        self.separator = separator


    def next(self):
        k = None
        for i in range(len(self.string)):
            if string[i] != self.separator:
                k = i
                break

        if self.string == "" and k == None:
            raise IndexError("index out of bounds")
        elif self.string == "":
            return self.string[k:]

        for i in range(len(self.string)):
            if (string[i] == self.separator):
                partition = self.string[k:i]
                self.string = self.string[i:]
                return partition
