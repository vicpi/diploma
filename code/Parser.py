# Verifies syntax by syntactic rules defined in "SyntacticRules" with EBNF
from Metadata import Rules
import InputStream
import Recognizer
import E
from Dictionary import Dictionary
from SemanticActions import SemanticActions
import AtrClasses
from Words import Words
from SS1 import SS1
from SS2 import SS2
from SS3 import SS3
from SS4 import SS4


# List of Rules.
# Each Rule consists of one or several RuleItems.
# Each RuleItem is a list.

class Parser:
    word = ""                             # word from input stream
    inputSymbol = ""                     # word class (inputstream)
    ruleSymbol = ""                        # symbol from rule (Rules)

    # Source code
    inputstream = InputStream.InputStream("source.pas")

    # Recognizing
    recognizer = Recognizer.Recognizer()

    RepeatableSymbols = []

    words = []

    def __init__(self):
        self.lexema = Dictionary()


    def Verify(self, source):
        """
        Effects: Verifies source for syntax correctness
        Requires: file "source" should exist
        """
        self.inputstream = InputStream.InputStream(source)
        self.nextToken()
        SemanticActions().initStandardTypes()
        self.checkAccordingToRule(Rules["programme"][0])
        d2 = SS3().pop()
        d22 = SS4().pop()
        dvicpi = SS3().trace()
        dvicpi2 = SS4().trace()
        d2.printed()
#        d22.printed()
#        print "File successfully parsed"

    def checkAccordingToRule(self, inRuleItem):
        """
        Effects: Checks programme on syntax correctness (one RuleItem)
        """
        RuleItem = self.subSequence(inRuleItem, 0, len(inRuleItem)-1)
        i = 0
        while i < len(RuleItem):
            self.ruleSymbol = RuleItem[i]
            self.nextRuleSymbol = self.getRuleSymbol(RuleItem, i)
            if self.isSemanticAction(self.ruleSymbol):
                i += 1
                continue
#            verify next rule symbol @here
            self.doSemanticAction(RuleItem, i)
            if self.nextRuleSymbol == "0":      # 0 is a special rule symbol after non-terminals in case to do this rule AFTER recursive search of rules
                i = i + 1
                continue
            if self.ruleSymbol == self.inputSymbol: self.addToDictionary()      # after doSemanticAction, otherwise symbol is double defined
            if self.ruleSymbol == "[[":
                index = self.findElement(RuleItem, "]]", i)
                if self.isDerivedFrom(RuleItem[i+1]):
                    RuleItem.pop(i)
                    RuleItem.pop(index-1)
                    i -= 1
                else:
                    i= index
            elif self.ruleSymbol == "{":
                index = self.findElement(RuleItem, "}", i)
                self.RepeatableSymbols = self.subSequence(RuleItem, i+1, index-1)

                if self.isDerivedFrom(RuleItem[i+1]):
#                    Insert RepeatableSymbols into RuleItem with index i
                    _i = i
                    for reSymbol in self.RepeatableSymbols:
                        RuleItem.insert(_i, reSymbol)
                        _i = _i + 1
                    i -= 1
                else:
                    i = index
            else:
                try:
                    self.treatSymbol()
                except E.ENotFoundRule:
                    return None
#                if foundAppropriateRule == None: return None
            i += 1

    def treatSymbol(self):
        """
        Effects: if is terminal, compares ruleSymbol with inputSymbol
        and reads next word from input stream.
        otherwise applies rule with appropriate left part
        """
        if self.isTerminal(self.ruleSymbol):
            if self.inputSymbol == self.ruleSymbol:
                self.nextToken()
            else:
                E.E(self.inputstream.lineNumber, self.inputstream.code).syntactic(
                            self.inputstream.lineNumber, self.ruleSymbol, self.word, "Inconformity")
        else:
            AppropriateRule = self.chooseAppropriateRule(self.ruleSymbol)
            if AppropriateRule == None:
                raise E.ENotFoundRule
#                return None
#                E.E(self.inputstream.lineNumber, self.inputstream.code).syntactic(
#                            self.inputstream.lineNumber, self.ruleSymbol, self.inputSymbol, "Inconformity")
            self.checkAccordingToRule(AppropriateRule)

    def subSequence(self, Sequence, startIndex, endIndex):
        """
        Effects: Returns sequence [ startIndex .. endIndex ]
        """
        i = startIndex
        Seq = []
        while i <= endIndex:
            Seq.append(Sequence[i])
            i += 1
        return Seq

    def findElement(self, Sequence, element, startindex):
        """
        Effects: Finds index of the specified element
        """
        while Sequence[startindex] != element:
            startindex += 1
        return startindex

    def isTerminal(self, symbol):
        """
        Terminals are always in right part of rules
        Non terminals are keys (left) of rules
        """
        return not Rules.has_key(symbol)

    def nextToken(self):
        """
        Reads from input stream word and defines its class
        Modifies: word, inputSymbol
        """
        if not self.inputstream.eof() :
            if self.word: 
                self.words.append(self.word)
                Words().push(self.word)
            self.word = self.inputstream.getWord()
            self.inputSymbol = self.recognizer.getClass(self.word)
            if self.inputSymbol == None:
                E.E(self.inputstream.lineNumber, self.word).e("WrongWord")

    def chooseAppropriateRule(self, ruleSymbol):
        """
        Effects: Returns rule that begins with symbol "inputSymbol"
        if more than one rule has this left part.
        """
        RightRule = Rules[ruleSymbol][0]
        for RightRule in Rules[ruleSymbol]:
            if (self.inputSymbol in self.findFirstSymbols(RightRule)):
                return RightRule
        return None

    def PossiblePrefixes(self ,Rule):
        """
        Effects: Return possible prefixes (possible input symbols)
        """
        i = 0
        First = []
        while i < len(Rule):
            if (Rule[i] == "[["):
                First.append(Rule[i+1])
                i = self.findElement(Rule, "]]", i+1)
            elif (Rule[i] == "{"):
                First.append(Rule[i+1])
                i = self.findElement(Rule, "}", i+1)
            else:
                First.append(Rule[i])
                return First
            i += 1
        return First

    def nextLevel(self, List):
        """
        Returns list with next level - non-terminals
        """
        out = []
        for symbol in List:
            if (self.isTerminal(symbol)):
                out.append(symbol)
            else:
                for _R in Rules[symbol]:
                    for symbol2 in self.PossiblePrefixes(_R):
                        out.append(symbol2)
        return out

    def findFirstSymbols(self, Rule):
        """
        Effects: Return list of first symbol
        """
        List = self.PossiblePrefixes(Rule)
        while (self.hasnonTerminals(List)):
            List = self.nextLevel(List)
        return List

    def hasnonTerminals(self, List):
        """
        Effects: Return True if list contains at least one non-terminal
        """
        for symbol in List:
            if not self.isTerminal(symbol):
                return True
        return False

    def isDerivedFrom(self, ruleSymbol):
        if (self.isTerminal(ruleSymbol)):
            return ruleSymbol == self.inputSymbol
        else:
            if ruleSymbol == self.inputSymbol:
                return True
            else:
                return (not self.chooseAppropriateRule(ruleSymbol) == None)

    def isSemanticAction(self, ruleSymbol):
        """
        Effects: Returns True if semantic action occurs and needs to be done
        """
        return ruleSymbol[0] == '#'

    def extractSemanticAction(self, ruleSymbol):
        """
        Effects: Return number of semantic action
        Requires: ruleSymbol must be in format "#\d+"
        """
        return ruleSymbol[1:]

    def addToDictionary(self):
        if (not self.lexema.isFound(self.word)):
            # @todo extract in comfortable place
            self.lexema.addSymbol( {"name" : self.word, 'class' : self.inputSymbol} )
            if self.inputSymbol == 'intConst':
                self.lexema.setObject( self.word, AtrClasses.AttrIntConst(self.word) )
            if self.inputSymbol == 'floatConst':
                self.lexema.setObject( self.word, AtrClasses.AttrFloatConst(self.word) )
            if self.inputSymbol == 'StringConst':
                self.lexema.setObject( self.word, AtrClasses.AttrStringConst(self.word) )

    def doSemanticAction(self, RuleItem, i):
        currentRuleSymbol = None
        if i+1 < len(RuleItem): currentRuleSymbol = RuleItem[i+1]
        if currentRuleSymbol is None: return False

        if self.isSemanticAction(currentRuleSymbol):
            semanticActionNumber = self.extractSemanticAction(currentRuleSymbol)
            if (semanticActionNumber.find(',') == -1):
                SemanticActions().switchAction(self.inputstream.lineNumber, semanticActionNumber, self.word)
            else:
                (semanticActionNumber1, semanticActionNumber2) = semanticActionNumber.split(',')
                SemanticActions().switchAction(self.inputstream.lineNumber, semanticActionNumber1, self.word)
                SemanticActions().switchAction(self.inputstream.lineNumber, semanticActionNumber2, self.word)
                

    def getRuleSymbol(self, RuleItem, i):
        if (i < len(RuleItem)):
            return RuleItem[i]
        else:
            return None