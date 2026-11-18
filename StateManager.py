    # Current layout goes:
    # Section 1: State Manager config

'''CAN ACCIDENTALLY CORRUPT DATA, DO NOT RELEASE THIS WITHOUT PATCHING'''

from os import makedirs

class StateManager:
    # This gets checked first, if it fails to match in the given filepath, abort the process and throw an error.
    version = 0.1
    versionString = "version = " + str(version)
    root = ""
    path = ""
    lineData = ""
    f = None
    # This will be the default config in case a preset is not given. If one is given, a system must be in place to retrieve it.
    statefields = []
    statevalues = []
    statetypes = []

    def __del__(self):                                     # Close an open file, if one was ever opened.
        self.closeFile()

    def __init__(self, root):
            # This function should set up the class to be completely ready to read/write any arbitrary data from/to a file by the end.
            # TODO: Currently does not work with filepaths which require creating folders. Fix that soon, please!
        self.ensureExists(root, is_directory=True)
        self.root = root

    '''
            # Without a built in version/safe-formatting check, external programs need to take care of that. Be careful what you download!!
    '''

    # Create a file with a matching filename passed to the object only if it does not already exist.
    # Gonna need a class for sanitizing strings. Too much variation in inputs and required outputs for an arbitrary function in this class alone.
    def ensureExists(self, path, is_directory=False):
        filepath = self.root + path
        if(is_directory == True):
            #print(f"Ensuring the directory '{filepath}' exists...")
            makedirs(filepath, exist_ok=True) # This requires sanitizing input. DONT INTENTIONALLY BREAK THIS IN TESTING!!!
            return 1
        else:
            try:
                with open(filepath, "x") as f:
                    #print(f"File '{filepath}' did not previously exist. Created missing file.")
                    return 0
            except FileExistsError:
                    #print(f"File '{filepath}' exists.")
                    return 1

    def closeFile(self):
        if(self.f != None):
            (self.f).truncate()
            (self.f).close()
            self.f = None
            #print(f"Closed the open file: {self.root + self.path}")
            self.path = ""

    def openFile(self, path):
        filepath = self.root + path
        self.closeFile()
        #print(f"Attempting to open a file: {filepath}.")
        exists = self.ensureExists(path)
        self.f = open(filepath, "r+", encoding="utf-8")
        self.path = path
        if(exists == 1):
            #print(f"Since {filepath} existed prior, old data will be overwritten!")
            return None

    def getStateFields(self):
        if(self.statefields == []):
            return []
        return self.statefields

    def getStateValue(self, field):
        i = 0
        while(i < self.statefieldcount):
            if(self.statefields[i] == field):
                return self.statevalues[i]
            i = i + 1
        return None

    def readData(self):
        line = ((self.f).readline()).strip()
        if(line != ""):
            return line
        else:
            #print(f"End of file {self.root + self.path} reached. Returning empty json object.")
            return "{}"

    def writeData(self, string):
        # Gonna need a class for sanitizing strings. Too much variation in inputs and required outputs for an arbitrary function in this class alone.
        (self.f).write(string)
