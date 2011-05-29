import Metadata
import sys

class E:
    symbolDoubleDefinition = "Semantic Error(%d): symbol %s is already defined (%s)"
    unknownAction = "Action %s is undefined (or not written in delegates)"
    unknownSymbol = "Unknown %s (%d): %s"

    def __init__(self, line, code):
        self.line = line
        self.code = code

    def e(self, e_class):
        metadata = Metadata.metadata
        print metadata["e"][e_class] % (self.code, self.line)
        sys.exit(0)

    def syntactic(self, line, expected, symbol, e_class):
        metadata = Metadata.metadata
        print metadata["e"][e_class] % (self.line, expected, symbol)
        sys.exit(0)

    def eof(self):
        metadata = Metadata.metadata
        print metadata["e"]["eof"] % (self.line, self.code)
        sys.exit(0)

    def semantic(self):
        metadata = Metadata.metadata
        print metadata["e"]["Semantic"] % (self.line, "symbol is used in wrong sense")
        sys.exit(0)

    def constDoubleDefinition(self, symbol):
        print self.doubleDefinition % (self.line, symbol, "const")
        sys.exit(0)

    def varDoubleDefinition(self, symbol):
        print self.symbolDoubleDefinition % (self.line, symbol, "variable")
        sys.exit(0)

    def doubleDefinition(self, symbol, type):
        print self.symbolDoubleDefinition % (self.line, symbol, type)
        sys.exit(0)

    def typeDoubleDefinition(self, symbol):
        print self.symbolDoubleDefinition % (self.line, symbol, "type")
        sys.exit(0)

    def undefinedAction(self, actionNo):
        print self.unknownAction % (actionNo)
        sys.exit(0)

    def typeUnknown(self, symbol):
        print self.unknownSymbol % ("type", self.line, symbol)
        sys.exit(0)

    def unknownIdentifier(self, symbol):
        print self.unknownSymbol % ("identifier", self.line, symbol)
        sys.exit(0)

    def incompatibleTypes(self, symbol, leftType, rightType):
        error = "incompatible types(%d): %s, %s"
        print error % (self.line, leftType, rightType)
        sys.exit(0)
        
    def conditionIsNotBoolean(self):
        error = "condition Is Not Boolean(%d)"
        print error % (self.line)
        sys.exit(0)
        
    def lastValueGreaterThanFirst(self):
        error = "First Value is Greater than Last(%d)"
        print error % (self.line)
        sys.exit(0)
        
        
class ENotFoundRule:
    def __init__(self):
        pass