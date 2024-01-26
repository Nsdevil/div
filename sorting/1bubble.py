'''
best,worst,avg : O{n^2}
'''
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)


'''
best : O{n}
worst,avg : O{n^2}
'''
def modified_bubble_sort(arr):
    for i in range(len(arr)-1):
        flag=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            break
        print(arr)

if __name__=='__main__':
    a=[int(i) for i in input().split()]
    bubble_sort(a)
    modified_bubble_sort(a)