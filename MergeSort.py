from random import randint

def MergeSort(arr,h,t):
    if h == t:
        array = [arr[h]]
        return array
    elif h < t:
        m = (h+t)/2
        arr1 = MergeSort(arr, h, m)
        arr2 = MergeSort(arr, m+1 , t)
        # merge
        merged = []
        i = 0
        j = 0
        while (i<=(m-h)) and (j<=(t-m-1)):
            if arr1[i] <= arr2[j] :
                merged.append(arr1[i])
                i+=1
            elif arr1[i] > arr2[j]:
                merged.append(arr2[j])
                j+=1
        while i<=m-h:
            merged.append(arr1[i])
            i+=1
        while j<=t-m-1:
            merged.append(arr2[j])
            j+=1
        return merged
    
array = []
for i in range(10):
    array.append(randint(0,20))
    
print(array)
golden = sorted(array)
print(golden)

sortedArray = MergeSort(array, 0, len(array)-1)
print(sortedArray)


            
            
		