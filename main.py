
names_list = []
search_text = "[name]"

with open("Input/Names/invited_names.txt") as file:
    names_list = file.readlines()


with open(r"Input/Letters/starting_letter.txt", "r") as letter:
    data = letter.read()
    for string in names_list:
        name = string.strip()
        new_data = data.replace(search_text, name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as new_letter:
            new_letter.write(new_data)
