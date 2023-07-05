def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = "Hello, Word! OpenAi is amazing."
output_sentence = reverse_words_in_sentence(input_sentence)
print(output_sentence)
