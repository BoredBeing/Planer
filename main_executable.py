import support_Planer as sp
#from planer import person as pp
import planer as p

filterOptions = p.AllParts
allPlans = p.AllPlans
allCommands = ["listNames","filter","getPlan","newInstance","","help"]


        

def listNames():
    string = ""
    for plan in allPlans:
        string = string + plan.name + "\n"
    print(string)
    
def filter():
    arguments = input("Enter Arguments")
    arguments.split(" ")
    checker = arguments[0].capitalize()
    if len(arguments)>= 1 and checker in filterOptions:
        list_index = filterOptions.index(checker)
        for plan in allPlans:
            plan.
        
    
    
     

def help():
    print(filterOptions)
    
def newInstance():
    p.newInstance()
    
def consoleInput():
    command = input("Enter Command: ")
    
    if command in allCommands:
        print("You pass")
        eval(command+"()")
    else:
        print("No Access")
        help()
        

consoleInput()