words = []
seen = set()    # track unique words
duplicate = set() # track duplicates

for i in range(5):
    words.append(input("Enter a words: "))
for word in words:
    if word in seen:
        duplicate.add(word)
    else:
        seen.add(word)
print(words)
print(f"Unique word: {len(seen)}")
print("Duplicate words: ", ", ".join(duplicate))