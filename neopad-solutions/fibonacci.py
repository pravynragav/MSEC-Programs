def calculate_fibonacci(n):
    # 1. Check for invalid negative input
    if n < 0:
        print("Invalid Input")
        return

    # 2. Print initial calculation header
    print(f"Fibonacci({n}):")
    
    # 3. Handle special base cases for 0 and 1
    if n == 0:
        print("Result: 0")
        return
    if n == 1:
        print("Result: 1")
        return

    # 4. Generate intermediate steps and calculate result
    # Although the prompt mentions recursion, the sample output displays 
    # a sequential progression from F(2) to F(n).
    a, b = 0, 1
    for i in range(2, n + 1):
        res = a + b
        print(f"F({i}) = {b} + {a} = {res}")
        a, b = b, res

    # 5. Final Result output
    print(f"Result: {b}")

if __name__ == "__main__":
    n = int(input())
    calculate_fibonacci(n)
