from random import shuffle


def shuffle_str_without_special_chars_displacement(string: str):
    special_chars = ",.!?;:'"

    special_chars_with_indices = [
        (char, index) for index, char in enumerate(string) if char in special_chars
    ]
    string_without_special_chars = [
        char for char in string if char not in special_chars
    ]

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

        first_char = word[0]
        last_char = word[-1]
        rest = word[1:-1]

        shuffled_rest = shuffle_str_without_special_chars_displacement(rest)

        result += first_char + shuffled_rest + last_char + " "

    return result


text = input("Enter a text you wanna mess:\n")
result = mess(text)

print(f"\n\nHere's the result:\n{result}")
