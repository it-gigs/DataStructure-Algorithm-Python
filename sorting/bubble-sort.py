def bubble_sort(a):
    for x in range(len(a)-1,0,-1):  
        for j in range(x):
              if a[j]>a[j+1]:
                  a[j],a[j+1] = a[j+1],a[j]

list = [6,3,1,5,9,8]
bubble_sort(list)
print(list)