import sys

# Recursive function to find the nth Tribonacci number
def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def main():
    try:
        # Read input N
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        result = []
        # Generate N numbers using recursion
        for i in range(n):
            result.append(str(tribonacci(i)))
        
        # Print output separated by space
        print(" ".join(result))
            
    except ValueError:
        pass

if __name__ == '__main__':
    main()
