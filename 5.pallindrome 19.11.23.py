#LAB 2 19/11/2023
#5.Write a function called get_palindrome ... 
def is_palindrome(s):
    
    return s == s[::-1]

def get_palindromes(input_string):
   
    words = input_string.split()

    palindromes = [word for word in words if is_palindrome(word)]

    return palindromes

user_input_string = input("Enter a string: ")
palindrome_list = get_palindromes(user_input_string)

print("Palindromes:", palindrome_list)
