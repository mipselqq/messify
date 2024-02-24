from random import shuffle

SPECIAL_CHARS = ",.!?;:'"


def shuffle_str_without_special_chars_displacement(string: str):
    special_chars_with_indices = [
        (char, index) for index, char in enumerate(string) if char in SPECIAL_CHARS
    ]
    string_without_special_chars = [
        char for char in string if char not in SPECIAL_CHARS
    ]

    # TODO: make sure that the string has always changed
    shuffle(string_without_special_chars)

    for char, index in special_chars_with_indices:
        string_without_special_chars.insert(index, char)

    return ''.join(string_without_special_chars)


def mess(text: str):
    result = ""

    for word in text.split(" "):
        if len(word) < 3:
            result += word + " "
            continue

        last_char_index = -1 if word[-1] not in SPECIAL_CHARS else -2
        last_char = word[last_char_index]
        first_char = word[0]
        rest = word[1:last_char_index]

        shuffled_rest = shuffle_str_without_special_chars_displacement(rest)

        result += first_char + shuffled_rest + last_char + " "

    return result


text = input("Enter a text you wanna mess:\n")
result = mess(text)

print(f"\n\nHere's the result:\n{result}")
