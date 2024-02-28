txt = input("Enter a String:")
freq = dict()
for word in txt:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        
freq_list = sorted(freq, key=freq.get, reverse=True)
print("The second most frequency:", freq_list[1])
