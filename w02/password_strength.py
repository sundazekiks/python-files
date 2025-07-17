
def word_in_file(word, case_sensitive=False):
    
    word_list = []
    toppasswords = []

    with open("w02/lists/toppasswords.txt", "r", encoding = "utf-8") as toppasswords_file:
        for line in toppasswords_file:
            toppasswords.append(line.strip())

    with open("w02/lists/wordlist.txt", "r") as dictionary_file:
        for line in dictionary_file:
            word_list.append(line.strip().lower())

    # Check if the password is in the toppasswords list
    
    if word in word_list and toppasswords:
        return True

    
            
def word_has_characters(word, character_list):
    
    count_lower = 0
    count_upper = 0
    count_digits = 0
    count_special = 0
    
    LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
    SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "\"", ",", ".", "<", ">", "?", "/", "`", "~"]
    
    for i in word:
        for a in LOWER:
            if i == a:
                count_lower += 1
        for a in UPPER:
            if i == a:
                count_upper += 1
        for a in DIGITS:
            if i == a:
                count_digits += 1
        for a in SPECIAL:
            if i == a:
                count_special += 1
                
    results = count_lower + count_upper + count_digits + count_special
    
    if results == len(word):
        return True
    else:
        return False
    

def word_complexity(word):
    
    #This will check the complexity of the password based on the number of different character types used.
    complexity = 0

    check_if_word_has_chars = word_has_characters(word)
    
    
def password_strength(password, min_length, strong_length):
    return 0
    

def main():
    passlength = 0
    
    while True:
        
        password = input("Enter a password: ")
        passlength = len(password)
        if password == "q" or password == "Q":
            print("Exiting the program.")
            print(passlength)
            break
        
        while bool(password):
            
            check_if_in_dictionary = word_in_file(password)
            check_if_word_has_char = word_has_characters("daniel")
            check_if_complexity = word_complexity(password)
            check_if_strength = password_strength(password, 8, 12)
            
            
            if check_if_in_dictionary:
                print("Password is too weak, it is a common word or password.")
                break
        
        
    
    
        
    
         

    
main()