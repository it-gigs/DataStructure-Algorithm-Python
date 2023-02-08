def merge_sort(a):
    n=len(a)
    temp = [None]*n
    sort(a,temp,0,n-1)
             

def sort(a,temp,low,up):
    if low == up: # only one element
        return

    mid = (low + up)//2

    sort(a, temp, low, mid)  # Sort a[low]....a[mid]
    sort(a, temp, mid+1, up) # Sort a[mid+1]....a[up]

    # Merge a[low]...a[mid] and a[mid+1]....a[up] to temp[low]...temp[up]
    merge(a, temp, low, mid, mid+1, up)
    	
    # Copy temp[low]...temp[up] to a[low]...a[up]
    copy(a, temp, low, up)
    

# a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]...temp[up2] 
def merge(a, temp, low1, up1, low2, up2):
    i = low1 
    j = low2 
    k = low1 

    while i <= up1  and j <= up2:
            if a[i] <= a[j]:
                temp[k] = a[i]
                i+=1
            else:
                temp[k] = a[j]
                j+=1
            k+=1
    
    while i <= up1:
                temp[k] = a[i]
                i+=1
                k+=1
            
    while j <= up2:
                temp[k] = a[j]
                j+=1
                k+=1

# copies temp[low]....temp[up] to a[low]...a[up]
def copy(a, temp, low, up):
    for i in range(low,up+1):
        a[i] = temp[i]
         
list = [6,3,1,5,9,8]
merge_sort(list)
print(list)