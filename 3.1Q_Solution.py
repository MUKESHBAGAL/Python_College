def print_pattern():
    for i in range(3):  # Loop over rows
        for j in range(6):  # Loop over columns
            if i == 0 and j == 6 // 2:
                print("* ", end="")
            elif i == 1 and (j >= i and j < 5 - 1):
                if i + 1 == j:
                    print(" ! ", end="")
                else:
                    print(" * ", end="")
            elif i == 2 and j < 6 - 1:
                print(" * ", end="")
            else:
                print("  ", end="")
        print()  # Move to the next line

print_pattern()

'''
OUTPUT::
      *     
   *  !  *     
 *  *  *  *  *  
 
 
'''


# Refrance code

"""
#include <stdio.h>

int main() {
    for(int i = 0; i < 3; i++) { // Loop over rows
        for(int j = 0; j < 6; j++) { // Loop over columns
            if(i == 0 && j == 6 / 2)
                printf("* ");
           else if(i==1&& (j>=i&&j<5-1)){
               if(i+1==j)
                 printf(" ! ");
              
               else 
                 printf(" * ");
           }
            else if(i == 2 && j < 6 - 1)
                printf(" * ");
            else 
                printf("  ");
        }
        printf("\n");
    }
    return 0;
}

"""
