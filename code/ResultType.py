## SS1 - Semantic Stack 1
## Singleton

class ResultType:

    class __impl:
        """ Implementation of the singleton interface """
        stack = []

        
        def __str__(self):
            s = ''
            for i in xrange(len(self.stack)):
                s += self.stack[i]
            return repr(self.stack)
            return s

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if SS1.__instance is None:
            # Create and remember instance
            SS1.__instance = SS1.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_SS1__instance'] = SS1.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)


    instance = None

    def getInstance(self):
        if self.instance:
            return self.instance
        else:
            self.instance = SS1()

