#This is a script for converting the ugly iBooks notes exports into a clean Markdown file
# *** Turn these into angi HTML file (could md also work?) and post them to a public website (similar to the notes
# app that has the spaced repitition system) and email a weblink to the person who emailed me
# also build up a massive email list and send out monthly upates
# see if there's a way to integrate with my existing notion page / profile (ZK)

import datetime
import sys

# Linked in the old notes files to this script
import os
ibook_highlighter_converter = os.path.dirname(os.path.abspath(__file__))
old_notes = open(os.path.join(ibook_highlighter_converter, 'ex_notes.txt'))
old_lines = old_notes.readlines()
#print(old_lines)

print('This message will be written to a file.')    

def convert_lines(lines):

    with open('formatted_notes.md', 'w') as md:
        #Create md output file and change the output to it
        sys.stdout = md
        for line in lines:
            if (line.startswith('August 3')):
            #change to datetime.date(%B, " " + %d, ", " + %Y)
                pass
            #elif line in text == Chaper + number format:
                #add line (unless it already exists) & remove the page #
            #maybe not neccessary elif line == '\n':
                #print('\n')
            else:
                md.write('### ' + line)
                #(+add page number from the line above if possible)
            #see if I need to do anything to account
        #Add line that drives people back to my website/twitter/youtube (my CTA)
        return md

print(convert_lines(old_lines))

print('hello')
    #with open('new_notes.md', 'w') as new_notes:
      #  print('test', file=new_notes)