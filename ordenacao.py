import time

# OK
def readTime(func, **kwargs):
    start_time = time.time()
    func(**kwargs)
    elapsed_time = time.time() - start_time
    retorno = "{0:.9f}".format(elapsed_time)
    return ("%s seg" % (retorno))

# OK
def bubbleSort(arr = []):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# OK
def insertionSort(arr = []):
    for i in range(0, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr

def mergeSort(arr = []):
    if len(arr) > 1:
        half = len(arr)//2
        arrLeft = arr[:half]
        arrRight = arr[half:]
        mergeSort(arr = arrLeft)
        mergeSort(arr = arrRight)
        i = j = k = 0
        while i < len(arrLeft) and j < len(arrRight):
            if arrLeft[i] < arrRight[i]:
                arr[k] = arrLeft[i]
                i += 1
            else:
                arr[k] = arrRight[j]
                j += 1
            k += 1
        while i < len(arrLeft):
            arr[k] = arrLeft[i]
            i += 1
            k += 1
        while j < len(arrRight):
            arr[k] = arrRight[j]
            j += 1
            k += 1
    return arr

#OK
def quickSort(arr = []):
    if arr:
        pv = (arr[0] + arr[len(arr)//2] + arr[len(arr) - 1])//3
        left = [x for x in arr if x < pv]
        right = [x for x in arr if x > pv]
        if len(left) > 1:
            left = quickSort(left)
        if len(right) > 1:
            right = quickSort(right)
        return left + [pv] * arr.count(pv) + right
    return []


with open('num.txt', 'r') as f:
    a = [int (x) for x in f.read().split()]
    print("\n\n")
    print("---------------------------------------------------------------")
    print("BubbleSort: {}".format(readTime(bubbleSort, arr = list(a))))
    print("---------------------------------------------------------------")
    print("InsertionSort: {}".format(readTime(insertionSort, arr = list(a))))
    print("---------------------------------------------------------------")
    print("QuickSort: {}".format(readTime(quickSort, arr = list(a))))
    print("---------------------------------------------------------------")
    print("\n\n")
    
    # print(bubbleSort(arr = list(a)))
    #print(insertionSort(arr = list(a)))
    # print(quickSort(arr = list(a)))