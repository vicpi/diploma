# Output data to file
class OutputStream:
    def __init__(self, fileName):
        self.f = open(fileName, "w")

    def writeWord(self):
        for word in self.words:
            self.f.write(word)
            self.f.write(' ')
        self.f.close()

    def add(self, word):
        self.words.append(word)



    words = []
    f = ""
