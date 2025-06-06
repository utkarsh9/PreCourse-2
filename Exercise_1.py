# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : N/A, no Leetcode link
# Any problem you faced while coding this : No

# Code identifies middle of sorted array and recursivelt searches subarrays for the value

def binarySearch(arr, l, r, x): 
  
  #write your code here
  if r >= l:
     mid = (r + l) // 2

     if arr[mid] == x:
        return mid
     
     elif arr[mid] > x:
        return binarySearch(arr, l, mid - 1, x)
     
     else:
        return binarySearch(arr, mid + 1, r, x)
  
  else:
     return -1
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
