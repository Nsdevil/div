'''
best,worst,avg : O{n*log base2 n}
space : O{1} + recursive stack space
'''

# def find_pivot(arr,low,high):
#     pivot=arr[low]
#     i,j=low,high
#     while i<j:
#         while arr[i]<=pivot and i<=high-1:
#             i+=1
        
#         while arr[j]>pivot and j>=low+1:
#             j-=1
        
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[low],arr[j]=arr[j],arr[low]
#     # print(arr,j)
#     return j

# def quick_sort(arr,low,high):
#     if low<high:
#         pivot=find_pivot(arr,low,high)
#         quick_sort(arr,low,pivot-1)
#         quick_sort(arr,pivot+1,high)

#         print(arr)

def find_pivot(arr,low,high):
    temp=low
    i,j=low,high
    while i<j:
        while arr[temp]>=arr[i] and i<=high-1:
            i+=1
        while arr[temp]<arr[j] and j>=low+1:
            j+=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[temp],arr[j]=arr[j],arr[temp]
    return j


def quick_sort(arr,low,high):
    if low<high:
        pivot=find_pivot(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)


if __name__=='__main__':
    a=[int(i) for i in input().split(' ')]
    quick_sort(a,0,len(a)-1)
    print(a)