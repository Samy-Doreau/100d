# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read template
with open('Input/Letters/starting_letter.txt') as starting_letter_file:
    starting_letter_template = starting_letter_file.read()

# Read names
with open('Input/Names/invited_names.txt', 'r') as invitees_file:
    invitees = invitees_file.readlines()
    invitees = [inv.replace('\n', '') for inv in invitees]


for invitee in invitees:
    letter_text = starting_letter_template.replace('[name]', invitee)
    with open(f'Output/ReadyToSend/letter_for_{invitee}.txt', 'w') as dest_file:
        dest_file.write(letter_text)
