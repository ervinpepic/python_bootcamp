from alphabet import alphabet
from logo import logo

def cesar(param_text, param_shift, param_direction):
    user_text = ""
    if param_direction == "decode":
        param_shift *= -1
    for chars in param_text:
        if chars in alphabet:
            position = alphabet.index(chars)
            new_position = position + param_shift
            new_chars = alphabet[new_position]
            user_text += new_chars
        else:
            user_text += chars
    print(f"Your {param_direction}d text is: {user_text}")

print(logo)

program_end = False
while not program_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    cesar(param_text=text, param_shift=shift, param_direction=direction)

    program = input("Type 'yes' if you want to do again. Else type 'no'. \n")
    if program == "no":
        program_end = True
        print("bye")