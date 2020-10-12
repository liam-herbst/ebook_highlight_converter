#This is a script for converting the ugly iBooks notes exports into a clean Markdown file

#import ~/home/liamherbst/github/projects/ibook_highlighter_converter/ex_notes.txt
import datetime
#from os import path

#test = open(os.path.join(home/liamherbst/github/projects/ibook_highlighter_converter/ex_notes.txt, 'ex_notes.txt'))

#print(test)

with open('ex_notes.txt, 'r') as old_notes:
    lines = old_notes.readlines()

    def convert_lines(lines):
        for line in lines:
            if (line.startswith('August 3')):
            #datetime.date(%B, " " + %d, ", " + %Y)
                pass
            #elif line in text == Chaper + number format:
                #add line (unless it already exists) & remove the page #
            #maybe not neccessary elif line == '\n':
                #print('\n')
            else:
                new_notes.write(line) 
                #(+add page number from the line above if possible)
            #see if I need to do anything to account

    with open('new_notes.md', 'w') as new_notes:
        print('test', file=new_notes)