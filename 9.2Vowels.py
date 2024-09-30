def count_vowels(items):
    count = 0
    collection_types = (list, tuple, set)

    for item in items:
        if isinstance(item, collection_types):
            for sub_item in item:
                if isinstance(sub_item, str):
                    count += check_valid_vowel(sub_item)

    for item in items:
        if isinstance(item, str):
            count += check_valid_vowel(item)

    return count

def check_valid_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = {}
    
    for char in string:
        if char in vowels:
            if char not in vowel_count:
                vowel_count[char] = 0
            vowel_count[char] += 1

    values = list(vowel_count.values())

    if values and len(set(values)) == 1:
        return 1  # All counted vowels have the same frequency
    elif values:
        return 1  # At least one vowel present
    return 0

# Test cases
print(count_vowels(['aauu', 'abcde', 'd', ['au']]))  # Output: 3
print(count_vowels(['eei', 'xyz', ['aeiou'], 'abc']))  # Output: 3
print(count_vowels(['aaa', 'eee', 'oo']))  # Output: 3
print(count_vowels(['bcdf', 'gh', 'ijkl']))  # Output: 0

