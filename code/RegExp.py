## Class for RegExp matching

import re

class RegExp:
    ## Returns TRUE if word matches pattern
    def match(self, word, pattern):
        if (re.compile(pattern).match(word)):
            return True
        else:
            return False
#    ----------------------------------------------------