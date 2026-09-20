def check_prime(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1

        return True
    
num=int(input("enter a num: "))
if check_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")    