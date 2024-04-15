import os
import support_Planer as sp


AllFiles = "C:/Users/Tobi/Documents/Boredom/Useful_scripts/Planer/plans/"
AllParts = ["Datum","Name","Place","People","Notes","Reminder"]
FileCount = len(os.listdir(AllFiles))
AllInstances = []
AllPlans = []

class Person:
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.lastname
        
def newInstance():
    with open(AllFiles+"plan_"+str(FileCount),"w") as f:
        for part in AllParts:
                f.write(part+": \n")
                ask = input("What should we put under: "+part+" \n")
                while ask != "":
                    f.write("-"+ask+" \n")
                    ask = input("Anything else? \n")
    
    reloadData()
            
    
def rawToPlan(fileRaw):
    fileLines = fileRaw.split("\n")
    content = []
    for line in fileLines:
        if line.startswith("-"):
            content.append(line[1:len(line)-1])
        else:
            content.append("\n")
    
    counter = -1
    Plan = sp.Plan()
    AllPlans.append(Plan)
    for element in content:
        if element == "\n":
            counter += 1
        else:
            if counter == 3:
                AllPeople = element.split(",")
                for person in AllPeople:
                    name = person.split(" ")
                    nPerson = Person(name[0],name[1])
                    string ="Plan."+str(Plan.allFunctions[counter])+"("+"nPerson"+")"
                    
                    
            elif counter == 0:
                string ="Plan."+str(Plan.allFunctions[counter])+"("+'"'+element+'"'+")"
                
            else:
                string = "Plan."+str(Plan.allFunctions[counter])+"("+'"'+"append"+'"'+","+'"'+element+'"'+")"
            eval(string)
    
    
        
def readAllInstances():
    for File in os.listdir(AllFiles):
        with open(AllFiles+File+"","r") as f:
            string = ""
            content = f.read()
            
            f.close()
            if os.stat(AllFiles+File).st_size == 0:
                os.remove(AllFiles+File)
                continue
            else:
                rawToPlan(content)
            
            
        
    
def reloadData():
    global FileCount
    FileCount = len(os.listdir(AllFiles))

readAllInstances()