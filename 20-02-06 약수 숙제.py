n =int(input("처리할 약수값:"))
t = 0
c=0
for x in range(1,n+1):
    if(n % x == 0):
        print(x,"는",n,"의 약수")
        t = t + x
        c= c+1
        
print(t,"은 모든 약수의 합")
print(c,"은 약수의 개수")    
