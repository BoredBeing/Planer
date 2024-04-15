import datetime

class Plan:
    attributes = ["date","name","personsInvolved","place","notes","reminder","passed","today"]
    def __init__(self):
        self.allFunctions = ["editDate","editName","editPlace","addPerson","editNotes","editReminder"]
        self.date = ""
        self.name = ""
        self.personsInvolved = []
        self.place = ""
        self.notes = ""
        self.reminder = ""
        self.passed = False
        self.today = False
        
          
    
         
        
    def __repr__(self):
        return("On the "+ self.date + ". You have " + self.name + ". At "+ self.place)
        
    def __str__(self):
        return("On the "+ self.date + ". You have " + self.name + ". At "+ self.place + " \n")
    
        
    def addPerson(self,person):
        self.personsInvolved.append(person)
        #print(person)
        
    def removePersonNr(self,number):
        if self.personsInvolved.length-1 >= number:
            self.personsInvolved 
        
    def removePersonName(self,name):
        for person in self.personsInvolved:
            Personname = person.firstname +" "+ person.lastname
            if name.lower() == Personname.lower():
                self.personsInvolved.remove(person)

    def editPlace(self,mode,text):
        
        mode = mode.lower()
        if mode== "a" or mode == "append":
            self.place += " "+text
        elif mode == "r" or mode == "remake":
            self.place = text
        else:
            help()
    
    def editDate(self,text):
        self.date = text
        date = self.date.split("-")
        conv = datetime.date(int(date[2]),int(date[1]),int(date[0]))
        now = datetime.datetime.now().date()
        self.passed = now > conv
        self.today = now == conv 
        
    def editNotes(self,mode,text):
        
        mode = mode.lower()
        if mode== "a" or mode == "append":
            self.notes += " "+text
        elif mode == "r" or mode == "remake":
            self.notes = text
        else:
            help()
        
    def editReminder(self,mode,text):
        
        mode = mode.lower()
        if mode== "a" or mode == "append":
            self.reminder += " "+text
        elif mode == "r" or mode == "remake":
            self.reminder = text
        else:
            help()
    
    def editName(self,mode,text):
        mode = mode.lower()
        if mode== "a" or mode == "append":
            self.name += " "+text
        elif mode == "r" or mode == "remake":
            self.name = text
        else:
            help()
    
             
    def help(self):
        print("Remember all the details can be edited later.")
        print("There are modes to edit: mode a or append for adding information to the already existing text.")
        print("And mode r or remake for doing it completely again")

    
