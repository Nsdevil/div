'''
best : O{n}
worst,avg : O{n^2}
'''
def insertation_sort(arr):
    out,inn=0,0
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
            inn+=1
        out+=1
        # print(out,inn)
        print(arr)
    print(out,inn)


if __name__=='__main__':
    a=[int(i) for i in input().split(' ')]
    insertation_sort(a)