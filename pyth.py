def plusMinus(arr):
    p=n=z=0
    for i in range(len(arr)):
        if arr[i]<0:
            n=n+1
        elif arr[i]>0:
            p+=1
        else:
            z+=1
    li=[round(p/len(arr),6),round(n/len(arr),6),round(z/len(arr),6)]
    return li
    
arr=[-4,3,-9,0,4,1]

print(plusMinus(arr))
