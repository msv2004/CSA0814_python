def replace_word(input_string, old_word, new_word):
    return input_string.replace(old_word, new_word)

input_string = "EPVP is HELLOWORLD"
old_word = "HELLOWORLD"
new_word = "PROGRAMWORLD"

result = replace_word(input_string, old_word, new_word)
print(result)
