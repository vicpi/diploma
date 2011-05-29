## SS1 - Semantic Stack 1
## Singleton

class Generator:

    class __impl:
        """ Implementation of the singleton interface """
        labels = 0
        variables = 0
        
        def getLabel(self):
            self.labels = self.labels + 1
            return "@Lid" + str(self.labels)
        
        def getVariable(self):
            self.variables = self.variables + 1
            return "@Vid" + str(self.variables)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Generator.__instance is None:
            # Create and remember instance
            Generator.__instance = Generator.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Generator__instance'] = Generator.__instance

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
            self.instance = Generator()

