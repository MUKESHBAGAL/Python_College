def print_pattern(n):
    for i in range(n):
        for j in range(2*n): 
            if j + i >= n and j - i <= n:
                if(i==n//2 and j==n):
                  print("! ", end="") 
                else:
                 print("* ", end="") 
            else:
                print("  ", end="") 
        print()


num = int(input("Enter a number :"))        
print_pattern(num)

'''
OUTPUT::
      *     
   *  !  *     
 *  *  *  *  *  
 
 
'''


# Refrance code

"""
#include <stdio.h>

void print_pattern(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2 * n; j++) {
            if (j + i >= n && j - i <= n) {
                if (i == n / 2 && j == n) {
                    printf("! ");
                } else {
                    printf("* ");
                }
            } else {
                printf("  ");
            }
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
