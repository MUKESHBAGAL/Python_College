def int_to_roman(number: int) -> str:
    roman = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    index = 0
    while number > 0:
        value = values[index]
        numeral = numerals[index]
        
        while number >= value:
            roman += numeral
            number -= value
        
        index += 1
    
    return roman


print(int_to_roman(1994))  # Output: 'MCMXCIV'
print(int_to_roman(50))    # Output: 'L'
print(int_to_roman(60))     # Output:'LX'
print(int_to_roman(4574))    # Output: 'MMMMDLXXIV'

