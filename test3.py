def longest_palindrome_substring(string):
    longest = ""
    for i in range(len(string)):
        # Verifica substrings centradas em um único caractere
        palindrome_odd = expand_around_center(string, i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd
        # Verifica substrings centradas em dois caracteres
        palindrome_even = expand_around_center(string, i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even
    return longest

def expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1:right]

input_string = "babad"
output_string = longest_palindrome_substring(input_string)
print(output_string)
