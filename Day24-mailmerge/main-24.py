with open("Input/Letters/starting_letter.txt") as outline:
    letter_lines = outline.readlines()

with open("Input/Names/invited_names.txt") as names:
    invitees = names.readlines()

for invitee in invitees:
    with open(f"Output/ReadyToSend/{invitee}-invitation.txt", "w") as invitation:
        for line in letter_lines:
            invitation.write(line.replace("[Name]", invitee.strip()))


