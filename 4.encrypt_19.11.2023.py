#LAB 2 19/11/2023
#4.Write a function called encrypt ... 
def encrypt(text, shift):
    encrypt_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26  
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26  
                elif shifted < ord('A'):
                    shifted += 26  

            encrypt_text += chr(shifted)
        else:
            encrypt_text += char  
    return encrypt_text

def decrypt(encrypt_text, shift):
    return encrypt(encrypt_text, -shift)  


user_text = input("Enter the text to encrypt: ")
shift_amount = int(input("Enter the shift amount: "))


encrypted = encrypt(user_text, shift_amount)
print("Encrypted:", encrypted)


decrypted = decrypt(encrypted, shift_amount)
print("Decrypted:", decrypted)
