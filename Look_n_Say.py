def Look_n_Say(a):
    lst = []
     
    c = 0
    while c < len(a):
         
        i= 1
        while c+1 < len(a) and a[c]==a[c+1]:
            c+= 1 
            i+= 1 
        lst.append(str(i)+a[c])
        c+= 1 
    return ''.join(lst)
    
row = int(input())
num = 1
for c in range (row):
    print(num)
    num = Look_n_Say(str(num))
     
  