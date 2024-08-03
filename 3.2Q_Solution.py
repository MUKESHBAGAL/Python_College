def print_pattern(n):
    if(n<3):
        print("Plese Enter a Greater than ",n," Input !!")
    for i in range(2*n-2):
        for j in range(2*n): 
            if (j + i == n and i < n) or \
               (j - i == n) or \
               (i - j == n - 2 and (i > n - 1 and i <= 2*n - 3)) or \
               (i + j == 3*n - 2 and (i > n - 1 and i <= 2*n - 3)):
                print("* ", end="") 
            elif i == n - 1 and j == n:
                print(n, " ", end="") 
            else:
                print("   ", end="") 
        print()

    
    for i in range(n):  
        for j in range(2*n - 1):  
            print(" * ", end="") 
        print() 

num = int(input("Enter a number :"))        
print_pattern(num)  

'''
OUTPUT::

Enter a number :3

          *         
     *        *     
 *        3        * 
     *        *             
 *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 

 
 
'''


# Refrance code

"""
#include <stdio.h>

void print_pattern(int n) {
    if (n < 3) {
        printf("Please Enter a Number Greater than %d\n", n);
        return;
    }

    for (int i = 0; i < 2*n - 2; i++) {
        for (int j = 0; j < 2*n; j++) {
            if ((j + i == n && i < n) || 
                (j - i == n) || 
                (i - j == n - 2 && (i > n - 1 && i <= 2*n - 3)) || 
                (i + j == 3*n - 2 && (i > n - 1 && i <= 2*n - 3))) {
                printf("* ");
            } else if (i == n - 1 && j == n) {
                printf("%d ", n);
            } else {
                printf("   ");
            }
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2*n - 1; j++) {
            printf(" * ");
        }
        printf("\n");
    }
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    print_pattern(num);

    return 0;
}



"""
