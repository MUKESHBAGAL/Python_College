def binary_subtraction(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    result = []
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        bit_a = int(bin_a[i])
        bit_b = int(bin_b[i])
        sub = bit_a - bit_b - borrow
        
        if sub < 0:
            sub += 2
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(sub))
    
    result = ''.join(result[::-1])
    return result.lstrip('0') or '0'

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))

print("Binary subtraction of the two numbers is:", binary_subtraction(a, b))

# OUTPUT:
    
# Enter the 1st Number: 5
# Enter the 2nd Number: 4
# Binary subtraction of the two numbers is: 1

# Enter the 1st Number: 5
# Enter the 2nd Number: 6
# Binary subtraction of the two numbers is: 111

# Enter the 1st Number: 15458
# Enter the 2nd Number: 5488
# Binary subtraction of the two numbers is: 10011011110010
