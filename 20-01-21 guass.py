import random as r

n=r.randint(1,100)

while True:
    g=int(input("번호 넣기"))

    if g==n:
        print("good")
        break


    if g<n:
        print("small")


    if g>n:
        print("big")
    
    
