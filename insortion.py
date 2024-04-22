def insortion(a):
    for i in range(1,len(a)):
        temp=a[i]
        k=i
        while(k>0 and temp<a[k-1]):
             a[k]=a[k-1]
             k=k-1
        a[k]=temp
    return a
        
a=[300,100,150,80,90,120]
print("before sorted the elements",a)
print("after performing sorted operation",insortion(a))
