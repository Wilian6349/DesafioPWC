def is_anagram_of_palindrome(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1

input_string = "racecar"
output = is_anagram_of_palindrome(input_string)
print(output)
