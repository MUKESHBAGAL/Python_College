def get_SS_SL(LIST):
    if len(LIST) < 2:
        return None, None
    
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in LIST:
        if num < smallest:
            second_smallest, smallest = smallest, num
        elif smallest < num < second_smallest:
            second_smallest = num

        if num > largest:
            second_largest, largest = largest, num
        elif largest > num > second_largest:
            second_largest = num

    if second_smallest == float('inf') or second_largest == float('-inf'):
        return None, None
    
    return second_smallest, second_largest

# User Input
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

result = get_SS_SL(user_list)
if result == (None, None):
    print("The list is too small or does not have distinct second smallest and second largest values.")
else:
    print(f"Second Smallest: {result[0]}, Second Largest: {result[1]}")

