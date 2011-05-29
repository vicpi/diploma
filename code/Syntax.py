# Victor Piskunov (c) 2008-2010
# Initial module for syntax checking.
# This is the main module. Checking syntax.
# It reads next lexem and analyzes it for syntax correction.
# Usage:
#    python Syntax.py <input file> <output file>
#    python Syntax.py source.pas o

import sys
import OutputStream
import Parser

# File names : source and output
if ( len(sys.argv) == 3 ):
    sourceFile = sys.argv[1]
    outputFile = sys.argv[2]
else:
    sourceFile = "source.pas"
    outputFile = "o"


# Result stream
outputStream = OutputStream.OutputStream('o')


parser = Parser.Parser()
parser.Verify(sourceFile)
