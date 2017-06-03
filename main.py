import datetime
import sys
import time
import os
import math

libs = []
version = 1.14
name = "Alexandra"
params = []
d = datetime.date.today()

class StopAI(Exception):
    pass

def yn(s):
    v = None
    while v != "Y" and v != "N":
        v = input(s)
    return v == "Y"

def slow_write(stm, c_speed, s):
    for c in s:
        stm.write(c)
        stm.flush()
        time.sleep(c_speed)

def init(libs_path, par):
    if not os.path.isdir(libs_path):
        os.makedirs(libs_path)
    libs = loadLibraries(libs_path)
    for i in par:
        params.append(libs[getCompiledPars("__PATH__")])

def start():
    try:
        init("VGF/libs/", ( 77, 8, 4, 3.0 ))
        setupMainCore()
        switch_AI("ON")
        startDiscussionProcess()
    except StopAI:
        pass

    print("Shutting down")
    time.sleep(3)
    print("Succesfully shut down!")
    time.sleep(2)
    return 0

def readLibrary(lib_path):
    with open(lib_path) as f:
        tab = f.read()
        tab = tab.split("\n")
        names = tab[0].split("\t")
        if maxTime == 0:
            maxTime = len(tab)
        new_tab = []
        for i in range(len(names)):
            new_tab.append([])
        for i in range(1, maxTime-1):
            split = tab[i].split("\t")   
            for j in range(0, len(split)):
                new_tab[j].append(float(split[j]))
        return names, new_tab

def loadLibraries(libs_path):
    libs = [ 0 ]
    for lib_file in os.listdir(libs_path):
        lib_path = os.path.join(libs_path, lib_file)
        if os.path.isfile(lib_path):
            libs.append(readLibrary(os.path.join(libs_path, lib_file)))
    return libs

def castToFloat(string):
    string = string.replace(',', '.')
    indE = string.find('E')
    if indE >= 0:
        return float(string[:indE]) * pow(10, float(string[indE + 1:]))
    else:
        return float(string)

def date():
    while True:
        v = d.day + d.month + d.year
        n_max = math.floor(math.sqrt(v))
        i = 0
        while i <= n_max:
            if v % i == 0:
                break
            i = i + 1
        if i > n_max:
            return d
        d += datetime.timedelta(days = 1)

def setupMainCore():
    time.sleep(0.5)
    print("Setting up main core...")
    time.sleep(3)
    print("Done")

def getCompiledPars(a):
    return 0

def switch_AI(a):
    print("Switching AI  ON...")
    time.sleep(12)
    if not yn("Modules [Recursive, Parser, Indentation] could not be loaded. Continue? [Y/N] "):
        raise StopAI()
    print("AI on")

n = 0
def send_to_AI(msg):
    global name, n
    cont = True
    if n == 0:
        time.sleep(4)
    elif n == 1:
        time.sleep(1)
    sys.stdout.write("<")
    sys.stdout.write(name)
    sys.stdout.write("> ")
    if n == 0:
        slow_write(sys.stdout, 0.1, "Bonjour\n")
    elif n == 1:
        slow_write(sys.stdout, 0.1, "Désolé j'ai pas très envie d'être en relation en ce moment\n")
        cont = False
    sys.stdout.flush()
    n = n + 1
    return cont

def startDiscussionProcess():
    print("Starting Discussion Process. Language set as:   DEFAULT(French)")
    time.sleep(24)
    print("Done")
    print("You can now engage conversation!")
    cont = True
    while cont:
        msg = input("<You> ")
        cont = send_to_AI(msg)

sys.exit(start())
