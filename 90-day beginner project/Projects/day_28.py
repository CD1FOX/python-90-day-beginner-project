def vowels_counter(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text_to_check = "Hello World"
print(vowels_counter(text_to_check))