def print_pattern():
    for i in range(8):  # Loop over rows
        for j in range(9):  # Loop over columns
            if (i == 0 or i == 4) and j == 9 // 2:
                print("  * ", end="")
            elif ((i == 1 or i == 3) and j % 2 == 0 and (j > 0 and j < 9 - 1 and j != 9 // 2)):
                print(" * ", end="")
            elif i == 2:
                if j == 9 // 2:
                    print(" 2 ", end="")
                elif j == 0 or j == 9 - 1:
                    print(" * ", end="")
                else:
                    print("  ", end="")
            elif i > 4 and i < 8:
                print(" * ", end="")
            else:
                print("  ", end="")
        print()  # Move to the next line

print_pattern()


'''
OUTPUT::
          *         
     *        *     
 *        2        * 
     *        *     
          *         
 *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 

 
 
'''


# Refrance code

"""
#include <stdio.h>
int main() {
    for(int i = 0; i<8; i++) { // Loop over rows
        for(int j = 0; j <9; j++) { // Loop over columns
           if((i==0 || i==4 ) && j==8/2)
                printf("  * ");
           else if((((i==1 || i==3) && j%2==0) && (j>0 && j<9-1 && j!=8/2)))
                printf(" * ");
           else if(i==2){
                if(j==8/2)            
                  printf("  2 ");
                else if((j==0&& j==9-1))
                  printf(" * ");
                else 
                printf("  ");
           }
           else if(i>4 && i<8)
                printf(" * ");
            else 
                printf("  ");
        }
        printf("\n");
    }
    return 0;
}


"""
