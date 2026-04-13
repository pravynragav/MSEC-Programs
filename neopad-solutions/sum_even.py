import sys

# The recursive function
def sum_even_numbers(arr, n):
    if n <= 0:
        return 0
    
    current = arr[n - 1]
    if current % 2 == 0:
        return current + sum_even_numbers(arr, n - 1)
    else:
        return sum_even_numbers(arr, n - 1)

# Robust input handling to avoid EOFError
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    # Slice the data to get only the array elements and convert to int
    arr = list(map(int, input_data[1:n+1]))
    print(sum_even_numbers(arr, n))
n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
print(sum_even_numbers(arr, n))
