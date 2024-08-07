def print_pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1): 
            if (j + i == n ) or \
               (j - i == n)or \
               (i-j==n and (i>n and i<2*n))or \
               (i+j==3*n and (i>n and i<2*n)):
                print("+ ", end="") 
            elif i == 2*n and j == n:
               	 print("- ", end="") 
            else:
                print("   ", end="") 
        print()

num = int(input("Enter a number :"))        
print_pattern(num)  
