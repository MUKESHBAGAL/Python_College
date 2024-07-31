def print_pattern():
    for i in range(6):  # Loop over rows
        for j in range(7):  # Loop over columns
            if i == 0 and j == 7 // 2:
                print("  * ", end="")
            elif i == 1 and j % 2 == 0 and (j > 0 and j < 7 - 1):
                print("  * ", end="")
            elif i == 2 and j % 2 == 1:
                if i + 1 == j:
                    print(" 2 ", end="")
                else:
                    print("  * ", end="")
            elif i == 3 and j % 2 == 1 and (j > 1 and j < 7 - 1):
                print(" * ", end="")
            elif (i > 3 and i < 6) and j < 7:
                print("  * ", end="")
            else:
                print("   ", end="")
        print()  # Move to the next line

print_pattern()

'''
OUTPUT::

           *          
        *      *       
     *      2      *    
          *     *    
 *   *   *   *   *   *   *  
 *   *   *   *   *   *   *    
 
 
'''



# Refrance code

"""
#include <stdio.h>

int main() {
    for(int i = 0; i < 6; i++) { // Loop over rows
        for(int j = 0; j < 7; j++) { // Loop over columns
            if(i==0 &&j==7/2)
                printf("  * ");
            else if(i==1 && j%2==0 && (j>0 && j<7-1)) 
                printf("  * ");
            else if(i==2 && j%2==1 ){
                if(i+1==j)            
                  printf("  2 ");
                else
                  printf("  * ");
            }
            else if(i==3 && j%2==1 && (j>1 && j<7-1))
              printf(" * ");
            else if((i>3 &&i<6) && j<7)
                printf(" *  ");
            else 
                printf("   ");
        }
        printf("\n");
    }
    return 0;
}

"""
