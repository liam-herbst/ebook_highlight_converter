#See if it's possible to modify the file name to reflect the book
## E.g. Formatted: Almanack of Naval

from datetime import datetime
import sys
import os

# Linked in the old notes files to this script
ibook_highlighter_converter = os.path.dirname(os.path.abspath(__file__))
old_notes = open(os.path.join(ibook_highlighter_converter, 'ex_notes.txt'))
old_lines = old_notes.readlines()

# Delete the page number (denoted by ", p. ") from the end of the chapter title line and appends it to the end of the next line
#a Not all chapter titles have this so I'll need to account for that (it shoudl be accounted for anyway)
## So chapter titles become duplicates and notes have accurate page numbers 

# Identify which lines are duplicates and switch them to h2

# Delete duplicate lines but leave the first instance of each duplicate

date_format = "%B %d, %Y"  

def convert_lines(lines):
        sys.stdout = fn
        for line in lines:
            # Identifies duplicate lines (chapters) and changes them to headers (h2)
            counter = 0 
            if line[counter] == line[counter + 1]:
                fn.write("<h2>" + line + "</h2>")
                counter += 1

            ## Removes duplicate lines 
            # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
            # https://careerkarma.com/blog/python-remove-duplicates-from-list/#:~:text=There%20are%20a%20couple%20of,you%20have%20into%20a%20set.

            # Checks to see if the line is a date and subsequently eliminates dates
            try:
                datetime.strptime(line, date_format)
                pass
            except ValueError:
                pass
            # Checks to see if the line is a duplicate (chapter titles are duplicates) and subsequently eliminates duplicates
            #if line in text == Chaper + number format:
                #add line (unless it already exists) & remove the page #
            #maybe not neccessary elif line == '\n':
                #print('\n')
            # Returns highlights and notes
            else:
                fn.write("<h2>" + line + "</h2>")
                #(+add page number from the line above if possible)
            #see if I need to do anything to account
        #Add line that drives people back to my website/twitter/youtube (my CTA)
        return fn

with open('formatted_notes.html', 'w') as fn:
    print("ending equation name [literally]", file=fn)

    print(convert_lines(old_lines))

with open('new_notes.html', 'w') as new_notes:
    print(holy, file=new_notes)