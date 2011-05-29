import re
from Metadata import metadata

class Recognizer:
    """
    Class for word classes. Gets classes of words.
    """
    def __init__(self):
        """
        Effects: create. Loads file configuration
        """
        # read from file table
        self.RegExp = metadata["re"]
        self.KeyWords = metadata["keywords"]

    def getClass(self, word):
        """
        Effects: Returns word class
        """
        c = None
        if (     (word in self.KeyWords)
                or (word in metadata["delimiters"])
                or (word in metadata["double"])
                or (word in metadata["conditional_delimiters"])
                or (word in metadata["multiplicative"])
                or (word in metadata["additive"])
                or (word in metadata["Relation"])
                ):
            c = word
        else:
            for r in self.RegExp.keys():
                if re.compile(r).match(word):
                    c = self.RegExp[r]
        return c

    def isOperator(self, token):
        if (     (self.getClass(token) == "Unary")
            or     (self.getClass(token) == "Multiplicative")
            or     (self.getClass(token) == "Additive")
            or  (self.getClass(token) == "Relation")
            ):
            return True
        else:
            return False;

    RegExp = {}
    KeyWords = []