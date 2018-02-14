#binary search

from random import randint

def BinarySearch(arr,l,r,x):
    if l <= r:      #<=, not <
       m = (l+r)/2
      
       if arr[m] == x:
           return m
       elif arr[m] < x:
           return BinarySearch(arr,m+1,r,x)
       elif arr[m] > x:
           return BinarySearch(arr,l,m-1,x)
    else :
        return -1
    

array = []
for i in range(10):
    array.append(randint(0,10))
    
x = randint(0,10)
array.sort()
print(array)
print("target: %d"%x)
index = BinarySearch(array,0,len(array)-1,x)
if index < 0 :
    print("target does not exist in array")
else :
    print("target index: %d"%index)