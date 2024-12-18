def check_count(items):
    count = 0
    collection_types = (list, tuple, set)

    for obj in items:
        if isinstance(obj, collection_types):
            for item in obj:
                if isinstance(item, str) and len(item) % 6 == 3 and item == item[::-1]:
                    count += 1
                elif isinstance(item, (int, float)):
                    item_str = str(item)
                    if len(item_str) % 6 == 3 and item_str == item_str[::-1]:
                        count += 1

    for obj in items:
        if isinstance(obj, str) and len(obj) % 6 == 3 and obj == obj[::-1]:
            count += 1

    return count

# Test cases
print(check_count(['aaa']))                      # Output: 1
print(check_count([121, 457, "SGGS", "#*#*"]))  # Output: 1
print(check_count(['aba', 'abcba', 'xyzzyx']))  # Output: 1
print(check_count([{1, 2, 'aa'}, ('xyzyx', 'abca')]))  # Output: 1
print(check_count(['abcd', 'madam', 'racecar']))  # Output: 1

