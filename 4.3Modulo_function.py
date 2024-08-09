def modulo_fun(num, deno):
    if deno == 0:
        raise ValueError("Denominator cannot be zero")
    
    if num < 0:
        num = -num
    if deno < 0:
        deno = -deno
    
    while num >= deno:
        num -= deno
    
    return num

num = int(input("Enter a numerator: "))
deno = int(input("Enter a denominator: "))
try:
    result = modulo_fun(num, deno)
    print("Result:", result)
except ValueError as e:
    print(e)

