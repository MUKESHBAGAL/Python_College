def str_to_int(text):
    result = 0
    for char in text:
        result = result * 10 + (ord(char) - ord('0'))
    return result

def Decimal_subtraction(a, b):
    l1 = list(a)
    l2 = list(b)
    sign=1
    l3 = []
    if(a<b):
    	a,b=b,a
    	sign=-1
    reversed_list1 = list(reversed(a))
    reversed_list2 = list(reversed(b))
    max_len = max(len(reversed_list1), len(reversed_list2))
    reversed_list1.extend('0' * (max_len - len(reversed_list1)))
    reversed_list2.extend('0' * (max_len - len(reversed_list2)))
    
    count = 0
    for i in range(max_len):
        temp = (str_to_int(reversed_list1[i]) - (str_to_int(reversed_list2[i]))) + count
        if temp < 0:
            temp += 10
            count = -1
        else:
            count = 0
        l3.append(temp)
    while len(l3) > 1 and l3[-1] == 0:
        l3.pop()
    
    return sign*''.join(map(str, reversed(l3)))

a = input("Enter the 1st Number: ")
b = input("Enter the 2nd Number: ")
print("Decimal subtraction of the two numbers is:", Decimal_subtraction(a, b))

