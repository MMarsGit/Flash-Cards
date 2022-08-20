isDebug = False
varList = []

def setState(state):
    if(state == True):
        isDebug = True
    else:
        isDebug = False
    
def debug(string):
    if(isDebug == True):
        print("DEBUG: " + string)

def log(string):
    print("LOG: " + string)

def addVariable(variable):
    myVarName = [ k for k,v in locals().iteritems() if v == variable][0]
    varList.append(myVarName)
    varList.append(variable)

def printVariables():
    for item in varList:
        print(varList[item] + ": ", "")
        print(varList[item] + 1)
        item += 1

