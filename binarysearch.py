# Program pro  binarni vyhledavani
 
def binary_search(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        # Pokud element je pritomny v middle (stred intervalu)
        if arr[mid] == x:
            return mid
 
        # Pokud element je mensi, nez mid (stred), tak bude pritomen v leve casti intervalu
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else - pritomen v prave casti
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element neexistuje 
        return -1
 
# Test
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Volani fce
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element je pritomen na indexu ", str(result))
else:
    print("Element neexistuje")