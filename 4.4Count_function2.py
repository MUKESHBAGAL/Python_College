def counter(string,substring,key):
	count = 0
    	start = 0
	if key==True:
		for i in range(len(string)- len(substring) + 1):
			if string[i:i + len(substring)] == substring:
				count = count + 1
		return count
		
	else:
		 while True:
        		start = str1.find(sub, start)
        		if start == -1:
            			break
        		count += 1
        		start += len(sub) 

    
    		return count
str1 = input("Enter the string: ")
sub = input("Enter the sub-string: ")
key=input(int("1.)	
print(counter(str1,sub,False))

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
