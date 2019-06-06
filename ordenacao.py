import time

def readTime(func, **kwargs):
    start_time = time.time()
    func(**kwargs)
    elapsed_time = time.time() - start_time
    retorno = "{0:.5f}".format(elapsed_time)
    return ("\n%s" % (retorno))

def bubbleSort(arr = []):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def insertionSort(arr = []):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp

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

def quickSort(arr=[]):
    pvs = 0
    if len(arr) > 3:
        pvs = (arr[0]+arr[len(arr)//2]+arr[len(arr)])//3
    else:
        pvs = arr[len(arr)]
    if len(arr) > 1:
        for i in range(0, len(arr) - 1):
            if arr[i] < pvs and arr[i + 1] > pvs:
                arrLeft = arr[:i]
                arrRight = arr[i:]
                quickSort(arr = arrLeft)
                quickSort(arr = arrRight)
