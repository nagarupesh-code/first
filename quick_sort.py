def quick(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        print(f"partitioned around pivot{arr[p]}:{arr[low:high+1]}")
        quick(arr,low,p-1)
        quick(arr,p+1,high)
    return arr
def partition(arr,low,high):
        pivot=low
        i=low
        j=high
        while i<j:
            while arr[i]<=arr[pivot] and i<high:
                i+=1
            while arr[j]>arr[pivot]:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[pivot],arr[j]=arr[j],arr[pivot]
        quick(arr,low,j-1)
        quick(arr,j+1,high)

list=[]
n=int(input("enter length of array"))
for i in range(n):
    val=int(input(f"element{i+1}:"))
    list.append(val)
res=quick(list,0,n-1)
print(res)