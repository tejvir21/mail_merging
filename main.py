with open(r"mail_merging\Input\Names\invited_names.txt") as name:
    names = name.readlines()

with open(r"mail_merging\Input\Letters\starting_letter.txt") as letter:
    data = letter.readlines()

for letters in range(len(names)):
    with open(r'mail_merging\Output\ReadyToSend\letter_for_'+names[letters].strip()+'.txt',"w") as new_file:
        line = data[0]
        line = line.replace('[name]',names[letters].strip())

        new_file.write(line)
        new_file.writelines(data[1:])