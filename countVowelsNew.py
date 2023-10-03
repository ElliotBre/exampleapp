reading = input("enter a string").lower()

vowels = [*map(reading.lower().count, "aeiou")]

print(f"There are {len(vowels)} vowels in this string")

