## Class for working with table of lexemes.

class Dictionary:

    class __impl:
        """ Implementation of the singleton interface """

        # Hash: identifiers, classes, attributes
        # {<word>:
        #    { name: <word>,
        #      class: <word_class>,
        #      object: <AttrObject>
        #    }
        # }
        lexems = {}
        ## Effects: Returns True if symbol is defined
        def isFound(self, symbol):
            return self.lexems.has_key(symbol)

        ## Effects: Adds symbol to table of lexemes
        def addSymbol(self, params):
            if not self.lexems.has_key( params['name'] ):
                self.lexems[ params['name'] ] = params

        def get(self, name):
            return self.lexems[ name ]

        def setObject(self, name, object):
            """ Set object to dictionary """
            self.lexems[ name ][ 'object' ] = object
            
        def deleteSymbol(self, key):
            if self.lexems.has_key( key ):
                del self.lexems[ key ]


    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Dictionary.__instance is None:
            # Create and remember instance
            Dictionary.__instance = Dictionary.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Dictionary__instance'] = Dictionary.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
    
    def has_key(self, key):
        return self.getInstance().has_key(key)

    instance = None

    def getInstance(self):
        if self.instance:
            return self.instance
        else:
            self.instance = Dictionary()

