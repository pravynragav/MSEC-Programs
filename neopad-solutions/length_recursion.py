# You are using Python
import sys

# Increase recursion depth to handle up to 101+ characters if necessary
sys.setrecursionlimit(200)

def calculate_length(s):
    # Recursive function to count characters
    def get_count(string):
        if string == "":
            return 0
        return 1 + get_count(string[1:])

    # Initial check: if the string is clearly too long, return None immediately
    # However, to be strictly recursive as per Johnny's goal:
    try:
        length = get_count(s)
        if length > 50:
            return None
        return length
    except RecursionError:
        return None
if __name__ == "__main__":
    input_string = input()
    length = calculate_length(input_string)

    if length is None:
        print("Invalid")
    else:
        print(f"The length of the string is: {length}")
