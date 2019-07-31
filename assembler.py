class node():
    def __init__(self, nodeId, nodeValue, nextNode = None):
        self.nodeId = nodeId
        self.nodeValue = nodeValue
        self.nextNode = nextNode

def excludeComment(line):
    newLine = line.split(';')[0]
    #print(len(newLine))
    if newLine.endswith('\n'):
        return newLine
    return newLine + '\n'

def getFuncao(line):
    if "global" in line:
        return True
    return False

def getSimbol(line):
    if "equ" in line or ":" in line:
        return line
    return ""


def readFile(file):
    s = ""
    with open(file, "r") as f:
        for i in f.readlines():
            i = excludeComment(i.lower())
            i = getSimbol(i)
            s = s + i
    return s

print(readFile("printFinal.asm"))
