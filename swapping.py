class Process:
    def __init__(self, name = "Unnamed", size = 1, id = 0, position = 0):
        self.name = name
        self.size = size
        self.position = position
        self.position = position
        self.id = id

    def __repr__(self):
        return "({}) {} -> {}M  - pos {}".format(self.id, self.name, self.size, self.position)

# Dificuldades: pensar na lógica de memória, usar classe? dicionário? uma classe para memória?
# Usar id implica usar classe para toda a memória

class Memory:
    memory = [None] * 100
    processList = []
    lastId = 1

# 1
    def load(self):
        name = input("Name: ")
        size = input("Size: ")
        method = input("Method: ")

        process = Process(name, size, self.lastId)
        self.lastId += 1

        if method is '0':
            self.firstMatch(process)
        elif method is '1':
            self.nextMatch(process)
        if method is '2':
            self.bestMatch(process)
        elif method is '3':
            self.wrostMatch(process)

# Em python nao da pra mudar o iterador dentro do for, logo essa opção não e util 
# 2
    # def show(self, prog = None):
    #     if prog is not None:
    #         print(prog)
    #     for i in range(0, len(self.memory)):
    #         if self.memory[i] is not None:
    #             print(self.memory[i])
    #             print(i)
    #             i += int(self.memory[i].size)
    #             print(i)

    def show(self, prog = None):
        if prog is not None:
            print(prog)
        for i in self.processList:
            print(i)

# 3
# deletar por id ou nome, primeira opcao
    # def delete(self, id = None, name = None):
    #     deleted = False
    #     if id is not None:
    #         for process in self.memory:
    #             if process.id == id:
    #                 process = None
    #                 deleted = True
    #         return True, deleted

    #     if name is not None:
    #         for process in self.memory:
    #             if process.nome == nome:
    #                 process = None
    #                 deleted = True
    #         return True, deleted

    #     return False, False

    def delete(self):
        deleted = False
        data = input("Nome ou Id: ")
        for i in range(0, len(self.memory)):
            process = self.memory[i]
            if process is not None:
                if process.id is ord(data)-48 or process.name is data:
                    self.processList.remove(process)
                    self.memory[i:i + int(process.size)] = [None] * int(process.size)
                    deleted = True
                    return True, deleted

# 4
    def freeSpace(self, mem = memory):
        print("{}M".format(mem.count(None)))

# 5
    def showState(self):
        for i in range(0, len(self.memory)):
            if self.memory[i] is not None:
                print("0x{} {}".format(i, self.memory[i]))
            else:
                print("0x{} None - 1M".format(i))

# 6
    def compress(self):
        lastNone = -1
        for i in range(0, len(self.memory)):
            process = self.memory[i]
            if process is None:
                for j in range(i, len(self.memory)):
                    process2 = process = self.memory[j]
                    if process2 is not None:
                        self.memory[i: i + int(process2.size)], self.memory[j: j + int(process2.size)] = self.memory[j: j + int(process2.size)], self.memory[i: i + int(process2.size)]
                        print("next")
                        break

    def firstMatch(self, process = None):
        size = int(process.size)
        for i in range(0, len(self.memory)):
            if self.memory[i] is None and self.memory[i : i + size].count(None) is size:
                self.memory[i : i + size] = [process] * size
                process.position = i
                self.processList.append(process)
                break

m = Memory()
opt = 0
menu = "\n1- Load Process into memory\n2- Show process in memory\n3- Remove a program from memory\n4- Show disponible space\n5- Show current state\n6- Compress memory\n7- Exit\n"

while(opt is not '7'):
    print(menu)
    opt = input()

# python nao tem switch case

    if opt is '1':
        m.load()
    elif opt is '2':
        m.show()
    elif opt is '3':
        m.delete()
    elif opt is '4':
        m.freeSpace()
    elif opt is '5':
        m.showState()
    elif opt is '6':
        m.compress()

