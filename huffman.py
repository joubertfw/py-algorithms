class node:

    def __init__(self, nodeValue = 0, nodeString = "", left = None, right = None):
        self.nodeValue = nodeValue
        self.nodeString = nodeString
        self.right = right
        self.left = left

    def __repr__(self):
        return "{} {}".format(self.nodeValue, self.nodeString)

def quickSort(arr = []):
    if arr:
        pv = arr[len(arr)//2].nodeValue
        left = [x for x in arr if x.nodeValue < pv]
        right = [x for x in arr if x.nodeValue > pv]
        if len(left) > 1:
            left = quickSort(left)
        if len(right) > 1:
            right = quickSort(right)
        return left + [pv] * arr.count(pv) + right
    return []


test = [[1, "a"], [2, "b"], [3, "c"], [4, "d"], [5, "e"]]
listNodes = []

for i in test:
    listNodes.append(node(nodeValue = i[0], nodeString = [i[1]]))

print(listNodes)

left = [x for x in listNodes if x.nodeValue < 3]

print(left)

