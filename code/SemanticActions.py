# Verifies semantic correctness of program defined in "Rules" as semantic actions

from Dictionary import Dictionary
import E
import AtrClasses
from SS1 import SS1
from SS2 import SS2
from SS3 import SS3
from SS4 import SS4
from Words import Words
from AtrClasses import *
from Metadata import Types

class SemanticActions:
    
    def getRow(self, _name, _class, _type):
        dict = {}
        dict['name'] = _name
        dict['class'] = _class
        dict['object'] = _type
        return dict
    
    def addToDictionary(self, dict):
        dictionary = Dictionary()
        dictionary.addSymbol( dict )

    def switchAction(self, lineNumber, rulenumber, symbol):
        self.lineNumber = lineNumber
        if (rulenumber == '0000'):
            self.action0000(lineNumber, symbol)
        elif (rulenumber == '1000'):
            self.action1000(lineNumber, symbol)
        elif (rulenumber == '2000'):
            self.action2000(lineNumber, symbol)
        elif (rulenumber == '3000'):
            self.action3000(lineNumber, symbol)
        elif (rulenumber == '4000'):
            self.action4000(lineNumber, symbol)
        elif (rulenumber == '55000'):
            self.action55000(lineNumber, symbol)
        elif (rulenumber == '5000'):
            self.action5000(lineNumber, symbol)
        elif (rulenumber == '6000'):
            self.action6000(lineNumber, symbol)
        elif (rulenumber == '7000'):
            self.action7000(lineNumber, symbol)
        elif (rulenumber == '8000'):
            self.action8000(lineNumber, symbol)
        elif (rulenumber == '9000'):
            self.action9000(lineNumber, symbol)
        elif (rulenumber == '10000'):
            self.action10000(lineNumber, symbol)
        elif (rulenumber == '11000'):
            self.action11000(lineNumber, symbol)
        elif (rulenumber == '12000'):
            self.action12000(lineNumber, symbol)
        elif (rulenumber == '14000'):
            self.action14000(lineNumber, symbol)
        elif (rulenumber == '15000'):
            self.action15000(lineNumber, symbol)
        elif (rulenumber == '16000'):
            self.action16000(lineNumber, symbol)
        elif (rulenumber == '17000'):
            self.action17000(lineNumber, symbol)
        elif (rulenumber == '18000'):
            self.action18000(lineNumber, symbol)
        elif (rulenumber == '19000'):
            self.action19000(lineNumber, symbol)
        elif (rulenumber == '20000'):
            self.action20000(lineNumber, symbol)
        elif (rulenumber == '16'):
            self.action16(lineNumber, symbol)
        elif (rulenumber == '17'):
            self.action17(lineNumber, symbol)
        elif (rulenumber == '18'):
            self.action18(lineNumber, symbol)
        elif (rulenumber == '19'):
            self.action19(lineNumber, symbol)
        elif (rulenumber == '20'):
            self.action20(lineNumber, symbol)
        elif (rulenumber == '21'):
            self.action21(lineNumber, symbol)
        elif (rulenumber == '22'):
            self.action22(lineNumber, symbol)
        elif (rulenumber == '23'):
            self.action23(lineNumber, symbol)
        elif (rulenumber == '26'):
            self.action26(lineNumber, symbol)
        elif (rulenumber == '27'):
            self.action27(lineNumber, symbol)
        elif (rulenumber == '28'):
            self.action28(lineNumber, symbol)
        elif (rulenumber == '29'):
            self.action29(lineNumber, symbol)
        elif (rulenumber == '30'):
            self.action30(lineNumber, symbol)
        elif (rulenumber == '31'):
            self.action31(lineNumber, symbol)
        elif (rulenumber == '200'):
            self.action200(lineNumber, symbol)
        elif (rulenumber == '210'):
            self.action210(lineNumber, symbol)
        elif (rulenumber == '220'):
            self.action220(lineNumber, symbol)
        elif (rulenumber == '230'):
            self.action230(lineNumber, symbol)
        elif (rulenumber == '240'):
            self.action240(lineNumber, symbol)
        elif (rulenumber == '250'):
            self.action250(lineNumber, symbol)
        elif (rulenumber == '260'):
            self.action260(lineNumber, symbol)
        elif (rulenumber == '270'):
            self.action270(lineNumber, symbol)
        elif (rulenumber == '280'):
            self.action280(lineNumber, symbol)
        elif (rulenumber == '290'):
            self.action290(lineNumber, symbol)
        elif (rulenumber == '299'):
            self.action299(lineNumber, symbol)
        elif (rulenumber == '2999'):
            self.action2999(lineNumber, symbol)
        elif (rulenumber == '2992'):
            self.action2992(lineNumber, symbol)
        elif (rulenumber == '300'):
            self.action300(lineNumber, symbol)
        elif (rulenumber == '310'):
            self.action310(lineNumber, symbol)
        elif (rulenumber == '311'):
            self.action311(lineNumber, symbol)
        elif (rulenumber == '330'):
            self.action330(lineNumber, symbol)
        elif (rulenumber == '340'):
            self.action340(lineNumber, symbol)
        elif (rulenumber == '350'):
            self.action350(lineNumber, symbol)
        elif (rulenumber == '360'):
            self.action360(lineNumber, symbol)
        else:
            E.E(lineNumber, 0).undefinedAction(rulenumber)

    def initStandardTypes(self):
        self.addToDictionary(self.getRow('byte', 'byte', AtrClasses.AttrWord()))
        self.addToDictionary(self.getRow('word', 'word', AtrClasses.AttrWord()))
        self.addToDictionary(self.getRow('shortint', 'shortint', AtrClasses.AttrLongInt()))
        self.addToDictionary(self.getRow('integer', 'integer', AtrClasses.AttrInt()))
        self.addToDictionary(self.getRow('longint', 'longint', AtrClasses.AttrLongInt()))
        self.addToDictionary(self.getRow('real', 'real', AtrClasses.AttrReal()))
        self.addToDictionary(self.getRow('double', 'double', AtrClasses.AttrDouble()))
        self.addToDictionary(self.getRow('boolean', 'boolean', AtrClasses.AttrBoolean()))
        self.addToDictionary(self.getRow('string', 'string', AtrClasses.AttrString()))
        self.addToDictionary(self.getRow('char', 'char', AtrClasses.AttrChar()))
        self.addToDictionary(self.getRow('1', 'int', AtrClasses.AttrIntConst('1')))
        
    def checkAssignment(self, left, right):
        leftType = self.getType(left)
        rightType = self.getType(right)
        if leftType == rightType: return True
        if Types[':='].has_key(leftType):
            return rightType in Types[":="][leftType]
        return False
    
    def getType(self, right):
        dictionary = Dictionary()
        isright = isinstance(right, AtrClasses.AttrElemAction) or isinstance(right, AtrClasses.AttrVar) or isinstance(right, AtrClasses.AttrIntConst) or isinstance(right, AtrClasses.AttrFloatConst)  or isinstance(right, AtrClasses.AttrStringConst) or isinstance(right, AtrClasses.AttrField) or isinstance(right, AtrClasses.AttrParam) or isinstance(right, AtrClasses.AttrRelation)
        if isright:
            rightType = right.type
        else:
            right = right.getValue()
            rightType = dictionary.get(right)
            if not rightType.has_key('object'): 
                E.E(self.lineNumber, 0).unknownIdentifier(right)
            rightType = rightType['object'].type
        return rightType
    
    ## Label @todo labels
    def action0000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).semantic(lineNumber)

    ## constant
    def action1000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).constDoubleDefinition(symbol)
        else:
            _attrConst = AtrClasses.AttrConst(symbol)
            ss1 = SS1()
            ss1.push(_attrConst)

    def action2000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        _attrInt = AtrClasses.AttrIntConst(symbol)
        ss1 = SS1()
        ss1.push(_attrInt)

    def action3000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        _attrString = AtrClasses.AttrStringConst(symbol)
        ss1 = SS1()
        ss1.push(_attrString)

    def action4000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        value = ss1.pop()
        name = ss1.pop()
        name.bind(value)
        dictionary = Dictionary()
        dictionary.setObject(name.name, name)

    def action55000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        # @todo problem Fields in record cannot have name equal to usual variables
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).varDoubleDefinition(symbol)
        else:
            _attrVar = AtrClasses.AttrVar(symbol)
            ss1 = SS1()
            ss1.push(None)
            ss1.push(_attrVar)

    def action5000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).varDoubleDefinition(symbol)
        else:
            _attrVar = AtrClasses.AttrVar(symbol)
            ss1 = SS1()
            ss1.push(_attrVar)

    def action6000(self, lineNumber, symbol):
#        symbol = symbol['name']        
        ss1 = SS1()
        dictionary = Dictionary()
        type = ss1.pop()
        while ss1.top() != None:
            name = ss1.pop()
            name.bindType(type['name'])
            dictionary.setObject(name.name, name)
        ss1.pop()

    def action8000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).typeDoubleDefinition(symbol)
        _attrUserType = AtrClasses.AttrUserType(symbol)
        ss1 = SS1()
        ss1.push(_attrUserType)

    def action7000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        record = ss1.pop();
        dictionary = Dictionary()
        # @todo make interface for array, record, diapason and id
        _class = dictionary.get(record.name.name)['class']
        dictionary.setObject(record.name.name, record)
        row = self.getRow(record.name.name, _class, record)

    def action18000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.push("record")

    def action9000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if not dictionary.isFound(symbol):
            E.E(lineNumber, 0).typeUnknown(symbol)
        type = dictionary.get(symbol)
        ss1 = SS1()
        ss1.push(type)

    def action20000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if not dictionary.isFound(symbol):
            E.E(lineNumber, 0).typeUnknown(symbol)
        type = dictionary.get(symbol)
        ss1 = SS1()
        ss1.push(type)

    def action12000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.push( AtrClasses.AttrIntConst(symbol) )

    def action10000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        _lower = ss1.pop()
        _upper = AtrClasses.AttrIntConst(symbol)
        ss1.push( AtrClasses.AttrRange(_lower, _upper) )
  
    def action14000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        _lower = ss1.pop()
        _upper = AtrClasses.AttrIntConst(symbol)
        ss1.push( AtrClasses.AttrRange(_lower, _upper) )

    def action15000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.push( "array" )

    def action16000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        _range = ss1.pop()
        ss1.pop()
        _arrayType = self.getRow('array', 'array', AtrClasses.AttrArray(_range))
        ss1.push( _arrayType )

    def action17000(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        if not dictionary.isFound(symbol):
            E.E(lineNumber, 0).typeUnknown(symbol)
        ss1 = SS1()
        _attrArray = ss1.pop()
        _attrArray['object'].setName(symbol)
        ss1.push( _attrArray )

    def action19000(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        _attrRecord = AtrClasses.AttrRecord()
        
        dictionary = Dictionary()
        while not ss1.top() == 'record':
            field_type = ss1.pop()
            while not ss1.top() is None:
                field = ss1.pop()
                _attrField = AtrClasses.AttrField(field)
                # local variables in record
                dictionary.deleteSymbol(field.name)
                _attrField.bindType(field_type['name'])
                _attrRecord.addField( _attrField )
            ss1.pop()

        ss1.pop()
        name = ss1.pop()
        _attrRecord.setName(name)
        ss1.push( _attrRecord )
        
    def action16(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.push('procedure')

    def action17(self, lineNumber, symbol):
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.push('function')

    def action18(self, lineNumber, symbol):
#        symbol = symbol['name']
        dictionary = Dictionary()
        ss1 = SS1()
        if dictionary.isFound(symbol):
            E.E(lineNumber, 0).doubleDefinition(symbol, 'procedure or function')
        ss1.push(symbol)
        ss1.push('proc_params')
        

    def action23(self, lineNumber, symbol):
        ' not done '
#        symbol = symbol['name']
        ss1 = SS1()
        ss1.pop()
        ss1.pop()

    def action21(self, lineNumber, symbol):
        ' not done '
#        symbol = symbol['name']
        dictionary = Dictionary()
        _attrProc = AtrClasses.AttrProc()
        ss1 = SS1()
        ss1.push(symbol)
        
        while not ss1.top() == 'proc_params':
            _type = ss1.pop()
            while not ss1.top() is None:
                attr = ss1.pop()
                attr.type = dictionary.get(symbol)
                _attrProc.addParam(attr)
            ss1.pop()
        ss1.pop()
        _name = ss1.pop()
        _attrProc.setName(_name)
        dictionary.setObject(_name, _attrProc)
        ss1.push(_attrProc)

    def action22(self, lineNumber, symbol):
        ' not done '
#        symbol = symbol['name']
        dictionary = Dictionary()
        ss1 = SS1()
        ss1.push(symbol)
        
        _restype = ss1.pop()
        _attrProc = ss1.pop()
        _attrProc.setResType(_restype)
        dictionary.setObject(_attrProc.name, _attrProc)

    def action26(self, lineNumber, symbol):
        ss1 = SS1()
        ss1.push(AttrDigit(symbol))

    def action27(self, lineNumber, symbol):
        dictionary = Dictionary()
        ss1 = SS1()
        if not dictionary.isFound(symbol):
            E.E(lineNumber, 0).unknownIdentifier(symbol)
        else:
            ss1.push(symbol)
    
    def action28(self, lineNumber, symbol):
        _attrElemAction = AtrClasses.AttrElemAction(symbol)
        ss1 = SS1()
        ss1.push(_attrElemAction)
    
    def action29(self, lineNumber, symbol):
        ss1 = SS1()
        right = ss1.pop()
        _attrElemAction = ss1.pop()
        left = ss1.pop()
        rightType = self.getType(right)
        leftType =  self.getType(left)
        type = _attrElemAction.getResultType(leftType, rightType)
        if type == None:
            E.E(lineNumber, 0).incompatibleTypes(symbol, leftType, rightType)
        _attrElemAction.left = left
        _attrElemAction.right = right
        _attrElemAction.type = type
        SS1().push(_attrElemAction)

    def action30(self, lineNumber, symbol):
        ss1 = SS1()
        dictionary = Dictionary()
        if not dictionary.isFound(symbol):
            E.E(lineNumber, 0).unknownIdentifier(symbol)
        ss1.push(AttrDigit(symbol))

    def action31(self, lineNumber, symbol):
        ss1 = SS1()
        right = ss1.pop()
        left = ss1.pop()
#        if not isinstance(left, AttrElemAction):
#            left = AttrDigit(left)
#        if not isinstance(right, AttrElemAction):
#            right = AttrDigit(right)
        _attrAssignment = AtrClasses.AttrAssignment(left, right) 
        if self.checkAssignment(left, right) ==False:
            E.E(lineNumber, 0).incompatibleTypes(symbol, self.getType(left), self.getType(right))
        ss3 = SS3()
        d2 = ss3.trace()
        if ss3.top() is not None:
            ss3.top().next = _attrAssignment
        ss3.push(_attrAssignment)
        

    def action200(self, lineNumber, symbol):
        _atrBend = AtrClasses.AttrBend(None, None)
        SS4().push(_atrBend)
        if SS3().top() is not None:
            SS3().top().next = _atrBend
        SS3().clear()

    def action210(self, lineNumber, symbol):
        SS4().top().first_action = SS3().top()
    
    def action220(self, lineNumber, symbol):
        SS3().pop()
        SS3().push(SS4().pop())
    
    def action230(self, lineNumber, symbol):
        _attrIf = AtrClasses.AttrIf()
        SS4().push(_attrIf)
        if SS3().top() is not None:
            SS3().top().next = _attrIf
        SS3().pop()
        
    def action240(self, lineNumber, symbol):
        _condition = SS1().pop()
        if _condition.type != "boolean":
            E.E(lineNumber, 0).conditionIsNotBoolean()
        else:
            SS4().top()._condition = _condition

    def action250(self, lineNumber, symbol):
        SS3().push(None)
        
    def action260(self, lineNumber, symbol):
        SS4().top()._then = SS3().pop()

    def action270(self, lineNumber, symbol):
        SS4().top()._else = SS3().pop()

    def action280(self, lineNumber, symbol):
        atr = SS4().pop()
        d2 = SS4().trace()
        SS3().push( atr )

    def action290(self, lineNumber, symbol):
        _attrWhile = AtrClasses.AttrWhile()
        SS4().push(_attrWhile)
        if SS3().top() is not None:
            SS3().top().next = _attrWhile
        SS3().pop()
    
    def action300(self, lineNumber, symbol):
        _condition = SS1().pop()
        if _condition.type != "boolean":
            E.E(lineNumber, 0).conditionIsNotBoolean()
        else:
            SS4().top()._condition = _condition

    def action310(self, lineNumber, symbol):
            d2 = SS3().trace()
            SS4().top().body = SS3().pop()

    def action311(self, lineNumber, symbol):
        _attrFor = AtrClasses.AttrFor()
        SS4().push(_attrFor)
        if SS3().top() is not None:
            SS3().top().next = _attrFor
        SS3().pop()
        
    def action330(self, lineNumber, symbol):
        if not Dictionary().isFound(symbol):
            E.E(lineNumber, 0).unknownIdentifier(symbol)
        else:
            lexem = Dictionary().get(symbol)
#            if lexem['object'].attr != 'AttrVar' or lexem['object'].type['object'].min
            SS4().top().parameter = lexem['object']
            
    def action340(self, lineNumber, symbol):
        first_value = SS1().pop()
        if self.checkAssignment(SS4().top().parameter, first_value):
            SS4().top().first = first_value
    
    def action350(self, lineNumber, symbol):
        SS4().top().step = Dictionary().get("1")['object']
        
    def action360(self, lineNumber, symbol):
        last_value = SS1().pop()
        attrFor = SS4().top()
        if self.checkAssignment(attrFor.parameter, last_value):
            attrFor.last = last_value
            if float(attrFor.last.getValue()) < float(attrFor.first.getValue()):
                E.E(lineNumber, 0).lastValueGreaterThanFirst()

    def action299(self, lineNumber, symbol):
        _attrElemAction = AtrClasses.AttrElemAction(symbol)
        ss1 = SS1()
        d2 = ss1.trace()
        ss1.push(_attrElemAction)

    def action2999(self, lineNumber, symbol):
        ss1 = SS1()
        d2 = ss1.trace()
        dictionary = Dictionary()
        right = ss1.pop()
        _attrRelation = ss1.pop()
        left = ss1.pop()
        rightType = self.getType(right)
        leftType = self.getType(left)
        type = _attrRelation.canBeCompared(leftType, rightType)
        if type == None:
            E.E(lineNumber, 0).incompatibleTypes(symbol, leftType, rightType)
        _attrRelation.left = left
        _attrRelation.right = right
        _attrRelation.type = 'boolean'
        SS1().push(_attrRelation)
        
    def action2992(self, lineNumber, symbol):
        _attrElemAction = AtrClasses.AttrRelation(symbol)
        ss1 = SS1()
        ss1.push(_attrElemAction)
        
    def action901(self):
        return 2
    