def q0(text):
    # q0 is the start state, which is also the state when the last character processed is not 'b'.
    if len(text) == 0:
        return "q0"  # Ended in state q0, which means the string doesn't end with 'b'
    symbol = text[0]
    if symbol in {'a', 'b'}:
        if symbol == 'b':
            return q1(text[1:])  # Move to state q1 if symbol is 'b'
        else:
            return q0(text[1:])  # Stay in state q0 if symbol is 'a'
    else:
        return "Rejected"  # Reject if symbol is not 'a' or 'b'

def q1(text):
    # q1 is the final state which is reached if the last character processed is 'b'.
    if len(text) == 0:
        return "q1"  # Ended in state q1, which means the string ends with 'b'
    symbol = text[0]
    if symbol in {'a', 'b'}:
        if symbol == 'b':
            return q1(text[1:])  # Stay in state q1 if symbol is 'b'
        else:
            return q0(text[1:])  # Move to state q0 if symbol is 'a'
    else:
        return "Rejected"  # Reject if symbol is not 'a' or 'b'

def dfa_ends_with_b(text):
    result = q0(text)  # Start processing from state q0
    if result == "q1":
        return "Accepted"  # If ended in state q1, the string ends with 'b'
    else:
        return "Rejected"  # If ended in state q0, the string does not end with 'b'

text = input("Enter a String: ")
print(dfa_ends_with_b(text))


#OUTPUT:  

"""
Enter a String: aaaa
Rejected

Enter a String: abab
Accepted

Enter a String: bbbbb
Accepted

Enter a String: abbbbbba
Rejected

Enter a String: abcbb 
Rejected

"""

