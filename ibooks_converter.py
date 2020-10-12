#This is a script for converting the ugly iBooks notes exports into a clean Markdown file

import datetime
import sys

# Linked in the old notes files to this script
import os
ibook_highlighter_converter = os.path.dirname(os.path.abspath(__file__))
old_notes = open(os.path.join(ibook_highlighter_converter, 'ex_notes.txt'))
old_lines = old_notes.readlines()
#print(old_lines)

new_notes = ''

def convert_lines(lines):
    with open('formatted_notes.md', 'w') as md:
        sys.stdout = md # Change the standard output to the file we created.
        print('This message will be written to a file.')
        #sys.stdout = original_stdout # Reset the standard output to its original value
        for line in lines:
            if (line.startswith('August 3')):
            #datetime.date(%B, " " + %d, ", " + %Y)
                pass
            #elif line in text == Chaper + number format:
                #add line (unless it already exists) & remove the page #
            #maybe not neccessary elif line == '\n':
                #print('\n')
            else:
                md.write(line)
                #(+add page number from the line above if possible)
            #see if I need to do anything to account
            '\n'
        return md

print(convert_lines(old_lines))

print('hello')
    #with open('new_notes.md', 'w') as new_notes:
      #  print('test', file=new_notes)