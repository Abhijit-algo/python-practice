num=float(input("enter  num : "))
divisor1=float(input("enter first divisor: "))
divisor2=float(input("enter second divisor : "))
if num%divisor1==0 and num%divisor2==0:
    print(f"{num} is divisible by {divisor1} and {divisor2}")
else:
    print(f"num is not divisible by two num")

