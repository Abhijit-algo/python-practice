def generate_fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
        
    return fib_sequence[:n]

if __name__ == "__main__":
    print("--- Fibonacci Series Generator ---")
    try:
        count = int(input("How many Fibonacci numbers do you want? "))
        if count <= 0:
            print("Please enter a number greater than 0.")
        else:
            result = generate_fibonacci(count)
            print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
