from asyncore import write


# with open('ervin-text.txt') as file:
#     content = file.read()
#     print(content)
with open("new_file.txt", mode='a') as w_file:
    w_file.write("Novi tekst dodat nakon starog")
print(w_file)
