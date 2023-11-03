string = "hi hello how are you"
# Split the string into words
words = string.split()

# Reverse each word and join them back with spaces
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)


print(result)
