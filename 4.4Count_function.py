def count_non_overlapping(str1, sub):
    count = 0
    start = 0

    while True:
        start = str1.find(sub, start)
        if start == -1:
            break
        count += 1
        start += len(sub) 

    return count

str1 = input("Enter the string: ")
sub = input("Enter the sub-string: ")

print(count_non_overlapping(str1, sub))

