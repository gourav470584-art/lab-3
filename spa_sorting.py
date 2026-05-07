
import random, time

def insertion_sort(arr):
    a=arr[:]
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a

def merge_sort(arr):
    if len(arr)<=1: return arr
    m=len(arr)//2
    left=merge_sort(arr[:m]); right=merge_sort(arr[m:])
    out=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            out.append(left[i]); i+=1
        else:
            out.append(right[j]); j+=1
    return out+left[i:]+right[j:]

def quick_sort(arr):
    if len(arr)<=1: return arr
    pivot=arr[-1]
    less=[x for x in arr[:-1] if x<=pivot]
    more=[x for x in arr[:-1] if x>pivot]
    return quick_sort(less)+[pivot]+quick_sort(more)

print("Correctness:", insertion_sort([5,2,9,1,5,6]))
