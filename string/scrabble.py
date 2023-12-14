# In this project, we want to find a word in a round of the game Scrabble
# For this, we have a random order of letters and want to rearrange them to form a word

# We need to address individual letters from the string

# 1. Step: create a string of letters
letters = "tdaa"

# 2. Step: rearrange the letters with the index
# Index 0 is the first letter
word = letters[1] + letters[2] + letters[0] + letters[3]

# 3. Step: print the word
print(word)
