# Word Frequency Counter

# Take input from the user
text = input("Enter a sentence or paragraph: ")

# Convert text to lowercase and split into words
words = text.lower().split()

# Create an empty dictionary to store word counts
word_count = {}

# Count word occurrences
for word in words:
    # Remove punctuation from each word
    word = "".join(char for char in word if char.isalnum())
    if word:  # skip empty strings
        word_count[word] = word_count.get(word, 0) + 1

# Print word frequencies
print("\nWord Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
