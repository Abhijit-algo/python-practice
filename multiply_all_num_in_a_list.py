def mul_list(numbers):
    total=1
    for i in numbers:
        total*=i
    return total;
print(f"multiply all num in list = {mul_list([2,5,6,3])}")