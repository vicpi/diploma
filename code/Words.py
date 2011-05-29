## Words - all read words
## Singleton

class Words:

    class __impl:
        """ Implementation of the singleton interface """
        stack = []

        def push(self, element):
            self.stack.append(element)

        def pop(self):
            if len(self.stack) > 0:
                result = self.stack.pop()
                return result
            else:
                return None

        def top(self):
            if len(self.stack) > 0:
                return self.stack[-1]
            else:
                return None
        
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
        if Words.__instance is None:
            # Create and remember instance
            Words.__instance = Words.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Words__instance'] = Words.__instance

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
            self.instance = Words()

