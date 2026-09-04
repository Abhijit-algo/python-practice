year=int(input("enter year : "))
if year%4==0 or year%400==0 and year%100!=0:
    print(f"year is lipyear")
else:
    print(f"no is not lipyear")