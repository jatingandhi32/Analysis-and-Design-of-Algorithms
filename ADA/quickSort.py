def quickSort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quickSort(array, low, index - 1)
        quickSort(array, index + 1, high)



	
def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):       
        if (array[j] < pivot):
            if i != j:
                array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i




array = list(map(int, input("Enter numbers: ").strip(" ").split(" ")))
size = len(array)
quickSort(array, 0, size - 1)
print("Sorted Array: ", array)
