a=1 
b=2 
t=0 
for i in range(3,24):
    g=(a+b)
    
    a=b
    b=g 
    if g%2==0:
        
        t=t+g
print(g)