
word = input("Input a word")

print("a","e","i","o","u")
print(*map(word.lower().count, "aeiou"))

