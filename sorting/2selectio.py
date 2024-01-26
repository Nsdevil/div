'''
best,worst,avg : O{n^2}
'''
def selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
        print(arr)



if __name__=='__main__':
    a=[int(i) for i in input().split(',')]
    selection_sort(a)