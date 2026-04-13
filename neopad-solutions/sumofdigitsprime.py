def check_sum_of_digits_prime(n):
    print(f"Calculating sum of digits for {n}")
    
    # Calculate sum of digits and print steps
    temp_n = n
    total_sum = 0
    # Handle digit extraction from right to left as shown in sample 1
    while temp_n > 0:
        digit = temp_n % 10
        total_sum += digit
        print(f"Extracted digit: {digit}, Current sum: {total_sum}")
        temp_n //= 10
        
    print(f"Total sum of digits: {total_sum}")
    
    # Primality check logic
    is_prime = True
    if total_sum < 2:
        is_prime = False
    else:
        for i in range(2, int(total_sum**0.5) + 1):
            if total_sum % i == 0:
                print(f"{total_sum} is divisible by {i}, hence not a prime number.")
                is_prime = False
                break
    
    # Final Result Output
    if is_prime:
        print(f"{total_sum} is a prime number.")
        print(f"Sum of digits: {total_sum} is a prime number.")
    else:
        print(f"Sum of digits: {total_sum} is not a prime number.")
n = int(input()) 
check_sum_of_digits_prime(n)
