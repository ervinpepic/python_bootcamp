# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as contacts_list:
    friends_list = contacts_list.readlines()

with open("Input/Letters/starting_letter.txt") as letter_content:
    readed_letter = letter_content.read()

    for friend_name in range(len(friends_list)):
        name = friends_list[friend_name].strip()
        formated_letter = readed_letter.replace("[name]", f"{name}")
        letter = formated_letter
        
        with open(f"Output/ReadyToSend/letter_for_{friends_list[friend_name]}.txt", 'w') as output_email:
            send_mail = output_email.write(letter)
