import re

with open("./books/frankenstein.txt") as f:
    letter_count = {}
    f_contents = f.read()
    result_string = re.sub(r'[^a-z]', '', f_contents.lower())
    for character in result_string:
        if character in letter_count:
            letter_count[character] += 1   
        else:
            letter_count[character] = 1
    

# sort letter count by value
letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))


print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(f_contents.split())} words found in the document")

# loop through the dictionary and for every key print the line The 'key' character was found 'value' times
for key, value in letter_count.items():
    print(f"The '{key}' character was found {value} times")
print("--- End report ---")