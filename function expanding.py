def  expand(lst):
    
    lst_2=[]
    for i in range(1,len(lst)):
        p=lst[i]-lst[i-1]
        lst_2.append(abs(p))
    
    r=True
    for j in range(1,len(lst_2)):
        if lst_2[j]<= lst_2[j-1]:
            r=False
            break
            
    return r
    
lst= list(map(int,input().split()))
print(expand(lst))
        