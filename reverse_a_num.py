num=int(input("enter num: "))
rev=0


while num!=0:
    b=num%10
    rev=(rev*10)+b
    num=num//10
    
print(f"rev no={rev}")
