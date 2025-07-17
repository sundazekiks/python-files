#Password Strength Checker

def word_in_file(word, wordfile, topfile, case_sensitive=False):
    
    word_list = []
    top_list = []

    
    with open(wordfile, "r") as word_file:
        
        for x in word_file:
            word_list.append(x.strip())
    with open(topfile, "r", encoding="utf-8") as top_file:
        for x in top_file:
            top_list.append(x.strip())
            
    # Check if the password is in the word list
    
    if case_sensitive:
        if word in top_list:
            print("Password is in the top passwords list.")
            return True
    elif not case_sensitive:
        if word.lower() in word_list:
            print("Password is in the word passwords list.")
            return True
    else:
        return False


def word_has_characters(word, character_list):
    
    count = 0
    
    for i in word:
        if i in character_list:
            count += 1
    
    if count > 0:
        return True
    else:
        return False



def word_complexity(word):
    
    complexity = 0
    
    LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    DIGITS=["0","1","2","3","4","5","6","7","8","9"]
    SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "\"", ",", ".", "<", ">", "?", "/", "`", "~"]
    
    # Check if the word has characters from each category
    check_lower = word_has_characters(word, LOWER)
    check_upper = word_has_characters(word, UPPER)
    check_digits = word_has_characters(word, DIGITS)
    check_special = word_has_characters(word, SPECIAL)
    
    
    if check_lower and check_upper and check_digits and check_special:
        complexity += 5
    elif check_lower and check_upper and check_digits:
        complexity += 4
    elif check_lower and check_upper and check_special:
        complexity += 4
    elif check_lower and check_special:
        complexity += 3
        
    return complexity
    

def  password_strength(word, min_length, strong_length):

    passlength = len(word)
    
    
    if passlength < min_length:
        return 1
    elif passlength == 10:
        return 2
    elif passlength > strong_length:
        return 6
    else:
        check_complexity = word_complexity(word)
        return check_complexity

            
    
def main():
    
    passlength = 0
    word_file = "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\wordlist.txt"
    top_file = "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\toppasswords.txt"
    
    while True:
        
        password = input("Enter a password: ").strip()
        passlength = len(password)
        
        while bool(password):
            
            check_if_in_dictionary = word_in_file(password, word_file, top_file, case_sensitive=False)
            check_pw_strength = password_strength(password, 10, 16)
            
            if check_if_in_dictionary:
                print(f"Password is a dictionary word and is not secure.  Strength: {check_pw_strength}")
                break
            
            if check_pw_strength <= 3:
                print(f"Password is too weak, it does not meet the strength requirements.  Strength: {check_pw_strength}")
                break
            
            if check_pw_strength >= 6:
                print(f"Password is long, length trumps complexity this is a good password. Strength: {check_pw_strength - 1}")
                break
            if check_pw_strength == 5:
                print(f"Password is secure, this is a good password. Strength: {check_pw_strength}")
                break
            
            if not check_if_in_dictionary and check_pw_strength >= 3:
                print(f"Password is secure. Strength: {check_pw_strength}")
                break
            
            


main()