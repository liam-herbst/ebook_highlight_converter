#This is a script for converting the ugly iBooks notes exports into a clean Markdown file

import ex_notes.txt

with open('ex_notes.txt') as notes:
    lines = notes.readlines()

    def convert_lines(lines):
        if line in text == #(insert date and time format (see codecademy cheatsheets)):
            delete line
        elif line in text == Chaper + number format:
            add line (unless it already exists) & remove the page #
        #maybe not neccessary elif line == '\n':
            print('\n')
        else:
            add line (+add page number from the line above if possible)
        #see if I need to do anything to account