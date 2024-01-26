'''
best,worst,avg : O{n*log base2 n}
space: O{n}
'''


# def merge(arr,low,mid,high):
#     x=[]
#     left,right=low,mid+1
    
#     while left<=mid and right<=high:
#         if arr[left]<=arr[right]:
#             x.append(arr[left])
#             left+=1
#         else:
#             x.append(arr[right])
#             right+=1
    
#     while left<=mid:
#         x.append(arr[left])
#         left+=1
#     while right<=high:
#         x.append(arr[right])
#         right+=1
    
#     for i in range(low,high+1):
#         arr[i]=x[i-low]
    
#     print(x,arr)

# def merge_sort(arr,low,high):
#     if low>=high:
#         return
    
#     mid=(low+high)//2
#     merge_sort(arr,low,mid)
#     merge_sort(arr,mid+1,high)

#     merge(arr,low,mid,high)

def merge_sort(arr,low,high):
    if low>=high:
        return
    
    mid=(low+high)//2

    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)

    merge(arr,low,mid,high)
    

def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=high:    
        temp.append(arr[right])
        right+=1
    
    for i in range(low,high-1):
        arr[i]=temp[i-low]

if __name__=='__main__':
    a=[int(i) for i in input().split(' ')]
    merge_sort(a,0,len(a)-1)
    print(a)
    