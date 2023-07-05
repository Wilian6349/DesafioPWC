def capitalize_after_comma(string):
    words = string.split()
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 or words[i - 1][-1] == ',' or word.lower() == "i'm":
            capitalized_word = word.capitalize()
        else:
            capitalized_word = word
        capitalized_words.append(capitalized_word)
    return ' '.join(capitalized_words)

input_string = "hello, how are you? i'm fine, thank you"
output_string = capitalize_after_comma(input_string)
print(output_string)
