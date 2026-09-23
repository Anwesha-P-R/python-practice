sentence = input("Enter a sentence: ")

print("\nNumber of characters:", len(sentence))
print("Number of spaces:", sentence.count(" "))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

print("First character:", sentence[0])
print("Last character:", sentence[-1])

word = input("Enter a word to search: ")

if word in sentence:
    print("The word exists in the sentence.")
else:
    print("The word does not exist in the sentence.")
