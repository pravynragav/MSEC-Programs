# You are using Python
import sys

def generate_pascals_row():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # Check constraints
    if n < 0 or n > 12:
        print("Invalid input")
        return

    # Base cases for Row 0 and Row 1
    current_row = [1]
    if n == 0:
        print(f"Final Pascal's Triangle Row: 1")
        return
    
    current_row = [1, 1]
    if n == 1:
        print(f"Final Pascal's Triangle Row: 1 1")
        return

    # Generation starting from Row 2 up to n
    prev_row = [1, 1]
    for i in range(2, n + 1):
        print(f"Generating row {i}:")
        print("Step 1: Start with 1")
        
        new_row = [1]
        step = 2
        for j in range(len(prev_row) - 1):
            val1 = prev_row[j]
            val2 = prev_row[j+1]
            sum_val = val1 + val2
            new_row.append(sum_val)
            print(f"Step {step}: {val1} + {val2} = {sum_val}")
            step += 1
            
        new_row.append(1)
        print(f"Step {step}: End with 1")
        
        row_str = " ".join(map(str, new_row))
        print(f"Final row {i}: {row_str}")
        prev_row = new_row

    print(f"Final Pascal's Triangle Row: {' '.join(map(str, prev_row))}")

if __name__ == "__main__":
    generate_pascals_row()
