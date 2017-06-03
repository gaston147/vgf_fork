import datetime as l
import sys
import time as tm

libs = []
version = 1.14
name = "Alexandra"
params = []
d=l.date.today()

def init(directory, par):
    libs = loadLibrairies(directory)
    for i in par:
        params.append(libs[getCompiledPars("__PATH__")])

def start():
    init("VGF\libs\\", (77,8,4,3.0))
    setupMainCore()
    switch_AI("ON")
    startDiscussionProcess()
                      
def readLibrary(path):
    file = open(path)
    tab = file.read()
    tab=tab.split("\n")
    names=tab[0].split("\t")
    if(maxTime==0):
        maxTime=len(tab)
    new_tab = []
    for i in range(len(names)):
        new_tab.append([])
 
    for i in range(1,maxTime-1):
        split=tab[i].split("\t")   
        for j in range(0,len(split)):
            new_tab[j].append(float(split[j]))
        
    print(maxTime)
    print(names)
    return names,new_tab

def loadLibraries(directory):
    for lib in directory:
        current=lib.open()
        libs.append(readLibrary(current)[1].PATH)

def castToFloat(string):
    string=string.replace(',','.')
    if'E' in string:
        return float(string[:-3])*pow(10,float(string[-2:]))
    else:
        return float(string)

def date():
    while True:
     v=d.day+d.month+d.year
     for i in range(2,v+1):
      if v%i==0:
       break
     if i==v:
      return d
      sys.exit(0)
     d+=l.timedelta(days=1)

def setupMainCore():
    tm.sleep(0.5)
    print("Setting up main core...")
    tm.sleep(1)
    print("Done")
    tm.sleep(2)


def loadLibrairies(directory):
    return [0]

def getCompiledPars(a):
    return 0

def switch_AI(a):
    print("Switching AI  ON...")
    tm.sleep(12)
    input("Modules [Recursive, Parser, Indentation] could not be loaded. Continue ?Y/N ")
    print("AI on")

def startDiscussionProcess():
    print("Starting Discussion Process. Language set as:   DEFAULT(French)")
    tm.sleep(20)
    print("Done")
    tm.sleep(4)
    print("You can now engage conversation!")
    input("<You>")
    tm.sleep(4)
    print("<Alexandra>Bonjour")
    input("<You>")
    tm.sleep(1)
    print("<Alexandra>Désolé j'ai pas très envie d'être en relation en ce moment")
    tm.sleep(1)
    print("Shutting down")
    tm.sleep(3)
    print("Succesfully shut down !")
    tm.sleep(2)
    exit(0)
    return 0
