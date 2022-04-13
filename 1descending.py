#using loop conditions to sort
arr=[10,18,12,9,2,5,1,20];
temp=0;
for i in range(0,len(arr)):
    for  j in range(i+1,len(arr)):
        if(arr[i]<arr[j]):     
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
print("Descending order of array elemets:")
for i in range(0,len(arr)):
    print(arr[i])
arr.sort()
arr.sort(reverse=True)
print("Descening order: ",arr)
    
