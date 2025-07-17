# Password Strength Checker

def word_in_file(word, wordfile, topfile, case_sensitive=False):
    with open(wordfile, "r") as word_file:
        word_list = [line.strip() for line in word_file]

    with open(topfile, "r", encoding="utf-8") as top_file:
        top_list = [line.strip() for line in top_file]

    if case_sensitive:
        if word in top_list:
            print("Password is in the top passwords list.")
            return True
    else:
        if word.lower() in word_list:
            print("Password is in the word passwords list.")
            return True

    return False


def word_has_characters(word, character_list):
    deter = [False] * len(character_list)

    for char in word:
        for i, group in enumerate(character_list):
            if char in group:
                deter[i] = True
                break

    return all(deter)


def word_complexity(word):
    LOWER = list("abcdefghijklmnopqrstuvwxyz")
    UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    DIGITS = list("0123456789")
    SPECIAL = list("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
    character_list = [DIGITS, LOWER, UPPER, SPECIAL]

    if not word_has_characters(word, character_list):
        return 0

    complexity = 0
    if any(c in LOWER for c in word): complexity += 1
    if any(c in UPPER for c in word): complexity += 1
    if any(c in DIGITS for c in word): complexity += 1
    if any(c in SPECIAL for c in word): complexity += 1

    return complexity


def password_strength(word, min_length, strong_length):
    length = len(word)
    complexity = word_complexity(word)

    if length < min_length:
        return 0
    elif length > strong_length:
        return complexity + 1
    else:
        return complexity + 1


def main():
    word_file = "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\wordlist.txt"
    top_file = "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\toppasswords.txt"

    while True:
        password = input("Enter a password: ").strip()

        if not password:
            print("Password cannot be empty.")
            continue

        in_dict = word_in_file(password, word_file, top_file, case_sensitive=False)
        complexity = word_complexity(password)
        strength = password_strength(password, min_length=10, strong_length=16)

        if in_dict:
            print(f"❌ Password is too common. Strength: {strength}")
        elif complexity < 3:
            print(f"❌ Not complex enough. Strength: {strength}")
        elif strength < 3:
            print(f"❌ Too weak overall. Strength: {strength}")
        else:
            print("✅ Password is strong enough.")
        print()


main()
