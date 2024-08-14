def modelo (n,d):
    q= int(n/d)
    rem= (n-(q*d))
    return rem 
    
m=int (input("enter m:"))
n=int (input("enter n:"))
print(modelo(m,n))
    
