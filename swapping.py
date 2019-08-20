class Process:
    def __init__(self, name = "Unnamed", size = 1, id = 0):
        self.name = name
        self.size = size
        self.id = id

    def __repr__(self):
        return "({}) {} -> {}M".format(self.id, self.name, self.size)

# Dificuldades: pensar na lógica de memória, usar classe? dicionário? uma classe para memória?
# Usar id implica usar classe para toda a memória

class Memory:
    memory = [None] * 100
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
    def show(self, prog = None):
        if prog is not None:
            print(prog)
        for i in range(0, len(self.memory)):
            if self.memory[i] is not None:
                print(self.memory[i])
                print(i)
                i += int(self.memory[i].size)
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
        data = input("Id or name: ")
        for process in self.memory:
            if process.id is data or process.name is data:
                process = None
                deleted = True
        return True, deleted

# 4
    def freeSpace(self, mem = memory):
        print("{}M".format(mem.count(None)))

# 5
    def showState(self):
        for i in range(0, len(self.memory)):
            if self.memory[i] is not None:
                print(self.memory[i])


    def firstMatch(self, process = None):
        size = int(process.size)
        for i in range(0, len(self.memory)):
            if self.memory[i] is None and self.memory[i : size].count(None) is size:
                self.memory[i : size] = [process] * size

m = Memory()
opt = 0
menu = "\n1- Load Process into memory\n2- Show process in memory\n3- Remove a program from memory\n4- Show disponible space\n5- Show current state\n7- Exit\n\n"

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


