def busqueda_lineal(value, arr: list):
    for index in range(len(arr)):
        if value == arr[index]: break
    return index

def busqueda_binaria(value, arr:list):
    start = 0
    mid = arr[int((len(arr)-1)/2)]
    end = arr[len(arr)-1]

    while end >= start:
        if value == arr[mid]:
            index = mid
            break
        elif value > arr[mid]:
            start = mid + 1
            mid = int((mid+end)/2)
        else:
            end = mid - 1
            mid = int((mid+start)/2)

    return index
