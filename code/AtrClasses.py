# This module contains all classes beginning with word "Attr"
# Every object in attribute table has type, and these classes define all possible types
from Metadata import Types
from Generator import Generator

class AttrObject:
    '''
    Abstract class, parent of all "Attr" classes
    '''
    def __init__(self, attr, name):
        self.attr = attr
        self.name = name

    def __str__(self):
        return self.name + "(" +self.attr + ")"
    
    def printLine(self, line):
        print line
        
    def printWord(self, word):
        print word


class AttrIntConst(AttrObject):
    '''
    Represents Integer type
    '''
    def __init__(self, name):
        self.value = int(name)
        AttrObject.__init__(self, "AttrIntConst", name)
        self.type = 'integer'

class AttrFloatConst(AttrObject):
    '''
    Represents Double type
    '''
    def __init__(self, name):
        self.value = float(name)
        AttrObject.__init__(self, "AttrFloatConst", name)
        self.type = 'double'
        
#    def __trunc__(self):
#        return self
class AttrStringConst(AttrObject):
    '''
    Represents String type
    '''
    def __init__(self, name):
        self.value = name
        AttrObject.__init__(self, "AttrStringConst", name)
        self.type = 'string'

class AttrConst(AttrObject):
    """
    Represents constant
    """
    def __init__(self, name):
        self.value = None
        AttrObject.__init__(self, "AttrConst", name)

    def bind(self, object):
        self.value = object

class AttrVar(AttrObject):
    """
    Represents variable
    """
    def __init__(self, name):
        #self.value = None
        AttrObject.__init__(self, "AttrVar", name)

    def bindType(self, type):
        self.type = type
        
    def __str__(self):
        return self.name + ' ' + self.type

""" Standard types """

class AttrInt(AttrObject):
    """
    Represents standard type "integer"
    """
    def __init__(self):
        self.min = -2147483648
        self.max = 2147483647
        self.size = 4
        AttrObject.__init__(self, "AttrInt", "integer")

class AttrLongInt(AttrObject):
    """
    Represents standard type "longint"
    """
    def __init__(self):
        self.min = -9223372036854775808
        self.max = 9223372036854775807
        self.size = 8
        AttrObject.__init__(self, "AttrLongInt", "longint")

class AttrShortInt(AttrObject):
    """
    Represents standard type "shortint"
    """
    def __init__(self):
        self.min = -32768
        self.max = 32767
        self.size = 2
        AttrObject.__init__(self, "AttrShortInt", "shortint")

class AttrWord(AttrObject):
    """
    Represents standard type "word"
    """
    def __init__(self):
        self.min = 0
        self.max = 4294967295
        self.size = 4
        AttrObject.__init__(self, "AttrWord", "word")

class AttrByte(AttrObject):
    """
    Represents standard type "byte"
    """
    def __init__(self):
        self.min = 0
        self.max = 255
        self.size = 1
        AttrObject.__init__(self, "AttrByte", "byte")

class AttrDouble(AttrObject):
    """
    Represents standard type "double"
    """
    def __init__(self):
        self.size = 8
        AttrObject.__init__(self, "AttrDouble", "double")

class AttrReal(AttrObject):
    """
    Represents standard type "real"
    """
    def __init__(self):
        self.size = 4
        AttrObject.__init__(self, "AttrReal", "real")

class AttrBoolean(AttrObject):
    """
    Represents standard type "boolean"
    """
    def __init__(self):
        self.size = 1
        AttrObject.__init__(self, "AttrBoolean", "boolean")

class AttrChar(AttrObject):
    """
    Represents standard type "char"
    """
    def __init__(self):
        self.min = 0
        self.max = 255
        self.size = 1
        AttrObject.__init__(self, "AttrChar", "char")

class AttrString(AttrObject):
    """
    Represents standard type "string"
    """
    def __init__(self):
        self.size = 255
        AttrObject.__init__(self, "AttrString", "string")

class AttrUserType(AttrObject):
    """
    Represents user type
    """
    def __init__(self, name):
#        self.size = 255
        AttrObject.__init__(self, "AttrUserType", name)

class AttrRecord(AttrObject):
    """
    Represents record type
    """
    def __init__(self):
        self.fields = []
        AttrObject.__init__(self, "AttrRecord", 'no yet')

    def addField(self, field):
        self.fields.append(field)

    def setName(self, name):
        self.name = name

class AttrField(AttrObject):
    """
    Represents record field
    """
    def __init__(self, name):
        AttrObject.__init__(self, "AttrField", name)
        
    def bindType(self, type):
        self.type = type
        
class AttrRange(AttrObject):
    '''
    Represents Range
    '''
    def __init__(self, _lower, _upper):
        self.lower = _lower
        self.upper = _upper
        AttrObject.__init__(self, "AttrRange", "range")
        
class AttrArray(AttrObject):
    '''
    Represents array
    '''
    def __init__(self, _range):
        self.range = _range
        AttrObject.__init__(self, "AttrArray", "array")
        
    def setName(self, _name):
        self.name = _name

                
class AttrProc(AttrObject):
    '''
    Represents procedure or function
    '''
    def __init__(self):
        self.params = []
        self.restype = None
        AttrObject.__init__(self, "AttrProc", "procfunc")
        
    def setName(self, name):
        self.name = name
        
    def addParam(self, _param):
        self.params.append(_param)
        
    def setResType(self, _restype):
        self.restype = _restype
        
    def isFunction(self):
        return self.restype is not None


class AttrParam(AttrObject):
    """
    Represents parameter in function or procedure
    """
    def __init__(self, name):
        AttrObject.__init__(self, "AttrParam", name)

    def bindType(self, type):
        self.type = type


class AttrElemAction(AttrObject):
    def __init__(self, name):
        AttrObject.__init__(self, "AttrElemAction", name)
        self.left = None
        self.right = None
        self.type = None
        
    # check whether types of operands are compatible
    # return result type of operation
    def getResultType(self, left, right):
        if Types[self.name].has_key(left) and Types[self.name][left].has_key(right):
            result = Types[self.name][left][right]
        else:  result = None
        return result
    
    def getValue(self):
        if self.name == "+":
            value = float(self.left.getValue()) + float(self.right.getValue())
        if self.name == "-":
            value = float(self.left.getValue()) -float( self.right.getValue())
        if self.name == "*":
            value = float(self.left.getValue()) * float(self.right.getValue())
        if self.name == "/":
            value = float(self.left.getValue()) / float(self.right.getValue())
        return str(value)

class AttrRelation(AttrObject):
    
    def __init__(self, name):
        AttrObject.__init__(self, "AttrRelation", name)
        self.left = None
        self.right = None
        self.type = None
        
    # check whether types of operands are compatible
    # return result type of operation
    def canBeCompared(self, left, right):
        # @todo compare types
        result = True
#        if Types[self.name].has_key(left) and Types[self.name][left].has_key(right):
#            result = Types[self.name][left][right]
#        else:  result = None
        return result
    
    def printed(self):
#        self.left.printed()
#        self.printWord(self.name)
#        self.right.printed()
        return self.left.getValue() + ' ' + self.name + ' ' + self.right.getValue()

    def __str__(self):
        return self.name

class AttrAssignment(AttrObject):
    def __init__(self, left, right):
        AttrObject.__init__(self, "AttrAssignment", "")
        self.left = left
        self.right = right
        self.next = None
        
    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right
    
    def printed(self):
        self.printLine(self.left.getValue()+ ":=" + self.right.getValue())

class AttrBend(AttrObject):
    def __init__(self, prev, next):
        AttrObject.__init__(self, "AttrBend", "")
        self.prev = prev
        self.first_action = None
        self.next = next
        
    def printed(self):
        if self.first_action is not None:
            self.first_action.printed()
            next = self.getnext()
            while next is not None:
                next.printed()
                next = next.next
                
    def getnext(self):
        return self.first_action.next
        
class AttrIf(AttrObject):
    def __init__(self):
        AttrObject.__init__(self, "AttrIf", "")
        self._condition = None 
        self._then = None
        self._else = None
        self.next = None
        
    def printed(self):
        label1 = Generator().getLabel()
        label2 = Generator().getLabel()
        self.printLine('if ' + self._condition.printed() + ' goto ' + label1)
        if self._else is not None: self._else.printed()
        self.printLine('goto ' + label2)
        self.printLine(label1 + ':')
        self._then.printed()
        self.printLine(label2 + ':')
        
            

class AttrWhile(AttrObject):
    def __init__(self):
        AttrObject.__init__(self, "AttrWhile", "")
        self._condition = None
        self.body = None
        self.next = None

class AttrFor(AttrObject):
    def __init__(self):
        AttrObject.__init__(self, "AttrFor", "")
        self.parameter = None 
        self.first = None
        self.last = None
        self.step = None
        self.body = None
        self.next = None
        
    def printed(self):
        first = str(self.first.getValue())
        last = str(self.last.getValue())
        label1 = Generator().getLabel()
        label2 = Generator().getLabel()
        self.printLine(self.parameter.name + ':=' + first)
        self.printLine(label1 + ':')
        self.printLine('if ' + self.parameter.name + ' > ' + last + ' goto ' + label2)
        self.body.printed()
        self.printLine(self.parameter.name + ' := ' + self.parameter.name + ' + 1')
        self.printLine('goto ' + label1)
        self.printLine(label2 + ':')
        
class AttrDigit(AttrObject):
    def __init__(self, digit):
        self.value = digit
        
    def getValue(self):
        return self.value
    
    def __str__(self):
        return self.value