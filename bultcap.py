a="hello"
b="world"
print(a+ " "+b)
c=a+ " "+b
words=c.split()
if len(words) >= 2 and len(words[1]) >= 2:
    second_word_second_character = words[1][1]
    print("Second word's second character:", second_word_second_character)
else:
    print("Not enough characters in the second word.")
