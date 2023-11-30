import random
import string

# Function to generate a password
def generate_password(length, favorite_word):
    # Define all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # If a favorite word is provided, add it to the end of the password
    if favorite_word:
        # Generate a random portion of the password excluding the favorite word
        random_part = ''.join(random.choice(characters) for _ in range(length - len(favorite_word)))
        password = random_part + favorite_word
    else:
        # Generate a password without a favorite word
        password = ''.join(random.choice(characters) for _ in range(length))
    
    # Shuffle the password characters for added randomness
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# Function to handle user input
def get_user_input():
    # Ask the user for the total length of the password
    length = int(input('Enter the full length of your password: '))
    
    while True:
        add_favorite = input('Do you want to add a favorite word? (yes/no): ').lower()
        if add_favorite in ['yes', 'y']:
            # If the user wants to add a favorite word, ask for it
            favorite_word = input('Enter your favorite word or digit to add to the password: ')
            break
        elif add_favorite in ['no', 'n']:
            favorite_word = ''
            break
        else:
            print('Wrong input. Please enter "yes" or "no".')
    
    return generate_password(length, favorite_word)

# Main execution starts here
generated_password = get_user_input()

# Print the generated password
print("Generated Password:", generated_password)
