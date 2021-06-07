import math

def binary_search(search, inputArray):
    inputArray.sort()
    return binary_search_recursive(search, inputArray, 0, len(inputArray)-1)

def binary_search_recursive(search, inputArray, l, r):
    if(r>=l):
        mid = math.floor((r+l)/2)
        if(inputArray[mid]==search):
            return mid
        elif(inputArray[mid] > search):
            return binary_search_recursive(search,inputArray,l,mid-1)
        else:
            return binary_search_recursive(search, inputArray,mid+1,r)
    else:
        return -1