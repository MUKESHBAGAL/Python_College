def change_case(text, style):
    if style in ['C', 'c']:
        result_capital = text.title()
        return result_capital
    elif style in ['S', 's']:
        result_small = text.lower()
        return result_small
    elif style in ['R', 'r']:
        result_random = ''.join(
            char.upper() if i % 2 == 0 else char.lower()
            for i, char in enumerate(text)
        )
        return result_random
    else:
        return "Invalid style"

# Test cases
print(change_case('SgGs', 'C'))  # Capitalize each word
print(change_case('SgGs', 'S'))  # Convert to lowercase
print(change_case('SgGs', 'R'))  # Alternating capitalization

