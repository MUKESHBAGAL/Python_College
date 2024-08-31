def manual_slice(string: str, start=0, end=None, step=1) -> str:
    if end is None:
        end = len(string)
        
    result = ""
    if step > 0:
        i = start
        while i < end and i < len(string):
            result += string[i]
            i += step
    elif step < 0:
        i = start
        while i > end and i >= 0:
            result += string[i]
            i += step
    
    return result

# Example usage:
print(manual_slice("abcdefghij", 2, 8, 2))  # Output: 'ceg'
print(manual_slice("abcdefghij", 8, 2, -2)) # Output: 'igec'
print(manual_slice("SGGS", 1, 3))           # Output: 'GG'

