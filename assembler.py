## todo: Make an table with predefined commands (MOV, JMP, etc)

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

def isFuncao(line):
    if "global" in line:
        return True
    return False

def isLabel(line):
    if ':' in line and '_' not in line:
        return True
    return False

def getSimbol(line):
    if "equ" in line or ":" in line:
        return line
    return ""

def readOpcodes(file):
    opcodeTb = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.split('#')[0]
            comm = line.split(' ')[0]
            code = line.split(' ')[1].split('\n')[0] # reading hex
            #code = int(code, 16) # hex to decimal
            #code = str(bin(code))[2:] # decimal to binary
            opcodeTb.append((comm, code))
    return opcodeTb

def readFile(file):
    hashTb = {}
    s = []
    labels = []
    functions = []
    isFuncaoControl = False
    with open(file, "r") as f:
        for line in f.readlines():
            line = excludeComment(line.lower())
            # line = getSimbol(line)
            s.append(line)
            if isLabel(line) and not isFuncaoControl:
                labels.append(line)
            if isFuncaoControl and '_' not in line:
                functions.append(line)
            isFuncaoControl = isFuncao(line)

    i = 0
    for label in labels:
        i = i + 1
        hashTb[label.split(':')[0]] = (label.split(':')[0], i)
    return labels, functions, hashTb


labels, functions, hashTb = readFile("printFinal.asm")

opcodeTb = readOpcodes("opcodes")

for i in opcodeTb:
    print(i)

# print(hashTb['opc1'])


# print("labels: \n\n" + labels)
# print("\n___________________________________________\n")
# print("functions: \n\n" + functions)
