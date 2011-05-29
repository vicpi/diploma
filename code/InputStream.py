# Module for reading lexems from text file with source code.
from Metadata import metadata
import RegExp
from Recognizer import Recognizer

class InputStream:
    ## Fields
    data = ""                        # Data from source file as a string
    delimiters = []                    # List of delimiters
    conditional_delimiters = {}
    whitespaces = []
    cursy = 0                        # Start symbol in string
    code = ""                        # Current line of code
    lineNumber = 1                    # Line of code number
    eol = metadata["eol"]            # EOL
    wordSequence = []
    
    def __init__(self, fileName):
        """
        Effects: Reads data from source file
        Requires: file "fileName" must exist on filesystem
        Modifies
        """
        self.delimiters = metadata["delimiters"]
        self.data = open(fileName, 'r').read()
        self.conditional_delimiters = metadata["conditional_delimiters"]
        self.whitespaces = metadata["whitespace"]

    def getWord(self):
        """
        Effects: gets word from input stream
        """
        regexp = RegExp.RegExp();
        begin = self.findBegin()
        fin = begin - 1
        old_start = begin                 # start of word
        rec = Recognizer()


#        Verify string
        if self.data[ begin:begin+1 ] == metadata["string"]:
            fin = self.data.find(metadata["string"], begin+1)
            word = self.data[ begin : fin+1 ]
            self.cursy = fin+1
#        Verify double delimiter
        elif self.data[ begin:begin+2 ] in metadata["double"]:
            word = self.data[ begin : begin+2 ]
            self.cursy = begin+2
        else:
            isEndLexem = 0
            while ((not isEndLexem) and (fin+1 < len(self.data))):
                fin = fin + 1
                if ((self.data[fin] in self.delimiters)
                    or (self.data[fin] in self.whitespaces)
                ):
                    isEndLexem = 1

                for _cond_delim in self.conditional_delimiters.keys():
                    if (self.data[fin] == _cond_delim):
                        if not (regexp.match(self.data[fin-1], self.conditional_delimiters[_cond_delim]["before"])
                        and regexp.match(self.data[fin+1], self.conditional_delimiters[_cond_delim]["after"])
                        ):
                            isEndLexem = 1
                if ((self.data[fin] in metadata["sign"]) and (len(self.wordSequence) > 0)
                    and (not rec.isOperator(self.wordSequence[len(self.wordSequence)-1]))
                    and (not regexp.match(self.data[fin-2 : fin], "[0-9]e"))
                    ):
                    isEndLexem = 1
            #-- while

            if begin == fin:
                word = self.data[begin]
                self.cursy = fin+1
            else:
                word = self.data[begin:fin]
                self.cursy = fin
        if old_start <> self.cursy:
            self.code = self.code + self.data[old_start : self.cursy]
        else:
            self.code = self.code + self.data[old_start]

        self.wordSequence.append(word)
        return word

    ## True if eof
    def eof(self):
        return (self.cursy >= len(self.data))

    def findBegin(self):
        """
        Requires: self.cursy is on whitespace
        Effects: Returns position of the first non-whitespace symbol.
        If it finds newline, count of lines is increased.
        Modifies: self.cursy points to first non-whitespace symbol
        """
        isWhiteSpace = 1
        while (isWhiteSpace == 1):
            if (self.data[self.cursy] in metadata["whitespace"]):
                if (self.data[self.cursy] == self.eol): self.lineNumber +=1
                self.cursy += 1
                continue
            elif ( (self.cursy+1 < len(self.data))
                    and (self.data[self.cursy : self.cursy+2] == metadata["comment"]["start"]) ):
                self.cursy = self.data.find(metadata["comment"]["end"])+2
            else:
                isWhiteSpace = 0
        return self.cursy
