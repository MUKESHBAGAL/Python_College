def check_validity(text):
    matching_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    opening_brackets = matching_pairs.keys()
    stack = []

    if len(text) == 0:
        return 1

    for symbol in text:
        if symbol in opening_brackets:
            stack.append(symbol)
        elif symbol in matching_pairs.values():
            if stack and matching_pairs[stack[-1]] == symbol:
                stack.pop()
            else:
                return -1

    return 1 if not stack else -1

t1 = '{[()]}'    
t2 = '{[('       
t3 = '{[<>()]}{}'  
t4 = '{[<]>}'    
t5 = ''          

print(check_validity(t1))  # Output: 1
print(check_validity(t2))  # Output: -1
print(check_validity(t3))  # Output: 1
print(check_validity(t4))  # Output: -1
print(check_validity(t5))  # Output: 1

