l=int(input("Enter lower range:"))
u=int(input("Enter upper range:"))
a=[]
a=[x for x in range(1,u+1) if(int(x**0.5))**2==x and sum(list(map(int,str(x))))]
print(a)
