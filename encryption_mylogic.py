# here we are going to do code, which encrypts our message and by using that key we decrypt our message

import random
import string

is_encrypt = True
original_string = string.punctuation + string.digits + string.ascii_letters 
original_string = list(original_string)
encrypted_messages = []
shuffled_strings = []

while is_encrypt:
    print()
    print("******************************************************************************")
    print("Type \'encrypt\' to encrypt the message or \'decrypt\' to decrypt the message")
    print("type \'show\' to show the encrypted messages")
    print("Type \'exit\' to exit the program")
    print("******************************************************************************")
    
    choice = input("Enter your choice: ").lower()
    if choice == "encrypt":
        message = input("Enter the message to encrypt: ")
        
        # Generate a new shuffled string
        shuffled_string = original_string.copy()
        random.shuffle(shuffled_string)
        shuffled_strings.append(shuffled_string)
        
        encrypted_message = ""
        for char in message:
            if char in original_string:
                index= original_string.index(char)
                encrypted_message += shuffled_string[index]
            else:
                print(f"Warning: Character '{char}' not found in original string. Skipping.")
                encrypted_message += char  # Add unrecognized characters as is
                
        encrypted_messages.append(encrypted_message)
        print(f"Encrypted message: {encrypted_message}")
        
    elif choice == "decrypt":
        message = input("Enter the message to decrypt: ")
        decrypt_message= ""
        
        # first check if encrypted message input exists in the list of encrypted messages
        if message in encrypted_messages:
            index_encrypted_message= encrypted_message.index(message)
            shuffle_string = shuffled_strings[index_encrypted_message]
            
            for char in message:
                if char in shuffle_string:
                    index = shuffle_string.index(char)
                    decrypt_message += original_string[index]
                else:
                    print(f"Warning: Character '{char}' not found in shuffled string. Skipping.")
                    decrypt_message += char  # Add unrecognized characters as is
                    
            print(f"Decrypted message: {decrypt_message}")
        else:
            print("Invalid message, your message is not in the list of encrypted messages. Please try again.")
            
    elif choice == "show":
        print("***********************")
        print("Encrypted Messages:")
        for i, msg in enumerate(encrypted_messages):
            print(f"{i + 1}. {msg}")
        print("***********************")

    elif choice == "exit":
        print("Exiting program. Goodbye!")
        is_encrypt = False
    
    else:
        print("Invalid choice. Please try again.")