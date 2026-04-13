def count_consonants(s, index=0, current_count=0):
    step = index + 1
    
    # Base case: string is empty/exhausted
    if index == len(s):
        print(f"Step {step}: The string is empty. Consonant count so far for alphabets is {current_count}")
        return current_count
    
    char = s[index]
    lower_char = char.lower()
    print(f"Step {step}: Checking '{char}'")
    
    is_consonant = False
    # Check if it's an alphabet and not a vowel
    if 'a' <= lower_char <= 'z':
        if lower_char not in ['a', 'e', 'i', 'o', 'u']:
            current_count += 1
            print(f"Step {step}: '{char}' is a consonant. Consonants so far: {current_count}")
            is_consonant = True
        else:
            print(f"Step {step}: '{char}' is not a consonant.")
            
    # Recursive call to the next character
    return count_consonants(s, index + 1, current_count)

input_str = input()
print("Tracing the steps:")
consonant_count = count_consonants(input_str)
print(f"Total consonants: {consonant_count}")
