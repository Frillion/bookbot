path = "./books/frankenstein.txt"
try:
    with open(path) as file:
        for line in file:
            file_contents = file.read()

except FileNotFoundError:
    file_contents = ""
    print("File Was Not Found")


def word_count(string):
    return len(string.split())

def char_count(string):
    char_dict = {}
    char_set = set( list(string.strip().lower()) )
    for char in char_set:
        if char in char_dict:
            continue

        char_dict[char] = string.count(char)

    return char_dict



print(f"--- Begin report of {path} ---")
print(f"{word_count(file_contents)} words foudn in the document")
char_counts = char_count(file_contents)
for char in char_counts:
    print(f"The '{char}' character was found {char_counts[char]} times")

print("--- End report ---")
