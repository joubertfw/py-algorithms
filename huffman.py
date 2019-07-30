class node:

    def __init__(self, nodeValue = 0, nodeString = "", nodeCode = "a", left = None, right = None):
        self.nodeValue = nodeValue
        self.nodeString = nodeString
        self.nodeCode = nodeCode
        self.right = right
        self.left = left

        if (left != None and right != None):
          self.nodeValue = right.nodeValue + left.nodeValue
          self.nodeString = "{} + {}".format(''.join(right.nodeString), ''.join(left.nodeString))

    def __repr__(self):
        return "[ {1} = {0} ]".format(self.nodeValue, ''.join(self.nodeString))

def insertionSort(arr = []):
  for i in range(0, len(arr)):
      temp = arr[i]
      j = i
      while j > 0 and temp.nodeValue > arr[j - 1].nodeValue:
          arr[j] = arr[j - 1]
          j -= 1
      arr[j] = temp
  return arr

def showCodes(node, cumulative = ""):
  if node != None:
    showCodes(node.left, cumulative + "1")
    showCodes(node.right, cumulative + "0")
    if node.left == None and node.right == None:
      print("{} = {}".format(''.join(node.nodeString), cumulative))

def readFromFile(fileName):
  a = ""
  print(a)
  

test = [[2, "e"], [3, "d"], [6, "a"], [5, "b"], [4, "c"], [1, "f"]]
listNodes = []

for i in test:
    listNodes.append(node(nodeValue = i[0], nodeString = [i[1]]))

ordArr = insertionSort(listNodes)

print('\n')
print(ordArr)
print('\n')

for i in range(len(ordArr) - 1, 0, -1):
  left = ordArr.pop()
  right = ordArr.pop()  

  left.nodeCode = left.nodeCode + "1"
  right.nodeCode = right.nodeCode + "0"

  ordArr.append(node(left = left, right = right))
  ordArr = insertionSort(ordArr)
  
  # mostrar passo a passo
  print(ordArr)
  print('\n')

print(ordArr)
print('\n')
showCodes(ordArr[0])

