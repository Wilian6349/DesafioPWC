def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

input_string = "Hello, World!"
output_string = remove_duplicates(input_string)
print(output_string)
