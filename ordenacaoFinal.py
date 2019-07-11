import time

# OK
def readTime(func, **kwargs):
    start_time = time.time()
    func(**kwargs)
    elapsed_time = time.time() - start_time
    retorno = "{0:.9f}".format(elapsed_time)
    return ("%s" % (retorno))

# OK
def bubbleSort(arr = []):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# OK
def selectionSort(arr = []):
    for i in range(0, len(arr)):
        menor = i
        for j in range(i, len(arr)):
            if arr[j] < arr[menor]:
                menor = j
        arr[i], arr[menor] = arr[menor], arr[i]
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

#OK
def mergeSort(arr = []):
    if len(arr) > 1:
        left = arr[ : len(arr)//2]
        right = arr[len(arr)//2 : ]
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1

    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
  
    for i in range(n, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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
    delta = 2000
    for i in range(delta, len(a)+1, delta):
        print("{}, {}, {}, {}, {}, {}".format(readTime(bubbleSort, arr = list(a)[:i]), readTime(insertionSort, arr = list(a)[:i]), readTime(selectionSort, arr = list(a)[:i]), readTime(mergeSort, arr = list(a)[:i]), readTime(heapSort, arr = list(a)[:i]), readTime(quickSort, arr = list(a)[:i])))


    # print(bubbleSort(arr = list(a)))
    # print(insertionSort(arr = list(a)))
    # print(quickSort(arr = list(a)))
    # print(heapSort(arr = list(a)))
    # print(selectionSort(arr = list(a)))
    # print(mergeSort(arr = list(a)))
