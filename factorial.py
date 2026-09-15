def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    return fact
num=int(input("enter number: "))
print(f"factorial={factorial(num)}")       
