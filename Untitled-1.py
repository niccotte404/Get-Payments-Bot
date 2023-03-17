from heapq import merge


def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 

if __name__ == '__main__':
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    
    mergeSort(arr1)
    mergeSort(arr2)
    
    print(*arr1)
    print(*arr2)
    
    a1 = arr1
    a2 = arr2
    
    for i in range(n1-1):
        if a1[i] == a1[i+1]:
            arr1.pop(i)
    
    for i in range(n2-1):
        if a2[i] == a2[i+1]:
            arr2.pop(i)
    
    print(*arr1)
    print(*arr2)
    