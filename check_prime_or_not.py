num=int(input("enter any num: "))
flag=1
i=2
while i<num-1:
    if(num%i==0):
      
        flag=0
        break

    i+=1  
if flag==1:
    print("no is prime")
else:
    print("no is not prime no")                  
