def insertion_sort(arr:list, type: str = "asc"):
    if type == "asc":
        for i in range(1, len(arr)):             
            var_elem = arr[i]                    
            j = i - 1                            
            while j >= 0 and var_elem < arr[j]:  
                arr[j+1] = arr[j]            
                j -= 1                        
            arr[j+1] = var_elem               
        return arr
    elif type == "desc":
        for i in range(1, len(arr)):             
            var_elem = arr[i]                    
            j = i - 1                            
            while j >= 0 and var_elem > arr[j]:  
                arr[j+1] = arr[j]            
                j -= 1                        
            arr[j+1] = var_elem
        return arr
    else:
        return "Error: El tipo de ordenamiento debe ser 'asc' o 'desc'"
            
def selection_sort(arr:list, type: str = "asc"):
    if type == "asc":
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr        
    elif type == "desc":
        n = len(arr)
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
    else:
        return "Error: El tipo de ordenamiento debe ser 'asc' o 'desc'"
    
def bubble_sort(arr:list, type: str = "asc"):
    if type == "asc":
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    elif type == "desc":
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    else:
        return "Error: El tipo de ordenamiento debe ser 'asc' o 'desc'"
    

