def gcd(a, b):
    steps = []
    
    def compute_gcd(x, y):
        # Base case: when second number reaches 0
        if y == 0:
            steps.append(f"gcd({x}, 0) reached. Final GCD: {x}")
            return x
        
        # Recursive step: calculate remainder and log the step
        remainder = x % y
        steps.append(f"gcd({x}, {y}) -> {x} % {y} = {remainder}")
        return compute_gcd(y, remainder)
    
    result = compute_gcd(a, b)
    return result, steps
if __name__ == "__main__":
    a, b = map(int, input().split())

    gcd_result, gcd_steps = gcd(a, b)
    lcm_result = (a * b) // gcd_result
    
    print("GCD Calculation Steps:")
    for step in gcd_steps:
        print(step)
    
    print(f"LCM Calculation: ({a} * {b}) // {gcd_result} = {lcm_result}")
    print(f"Final LCM: {lcm_result}")
