import random

def guess_number(entry_fee):
    ran_num = random.randint(1, 100)
    rewards = {1: 5, 2: 3, 3: 2, 4: 1.5, 5: 1}
    count = 0
    
    while count < 5:
        num = int(input("Guess The Number: "))
        if num < ran_num:
            print("Number is larger than", num)
            count += 1
        elif num > ran_num:
            print("Number is smaller than", num)
            count += 1
        else:
            print("Congrats, your guess is right!!")
            return entry_fee * rewards[min(count + 1, 5)] 
            
    print("Sorry, you've used all your attempts. The number was:", ran_num)
    return entry_fee * rewards[5] 

print("Welcome to the Guess Number Game!")
print("1ST PRIZE: 5 TIMES OF ENTRY FEE")
print("2ND PRIZE: 3 TIMES OF ENTRY FEE")
print("3RD PRIZE: 2 TIMES OF ENTRY FEE")
print("4TH PRIZE: 1.5 TIMES OF ENTRY FEE")
print("5TH: RETURN YOUR ENTRY FEES")
entry_fee = int(input("Entry Fee: "))
print("Guess a number between 1 and 100.")
print("Congrats, you win", guess_number(entry_fee), "Rupees!")

