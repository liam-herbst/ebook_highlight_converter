#See if it's possible to modify the file name to reflect the book
## E.g. Formatted: Almanack of Naval
#Ideally I'll be able to automatically make a bulleted list for the notes under each chapter 
#for the time being I could just add a "- " for each item so I can input that way into notion

### Import modules and files ###
from datetime import datetime
import sys
import os

original_notes = open('ex_notes.txt', 'r')
original_lines = original_notes.readlines()

# Confirm highlights properly converted to a list
#print(type(original_lines))

# Confirm highlights properly outputted
#print(original_lines)

### Format Import ### 
def remove_spaces(original_lines):
    removed_space_lines = []
    for line in original_lines:
        if line.startswith('\n'):
            pass
        elif line.endswith('\n'):
            remove_line_space = line[:-1]
            removed_space_lines.append(remove_line_space)
        else:
            removed_space_lines.append(line)
    return removed_space_lines

# Save output
removed_spaces = remove_spaces(original_lines)

# Test
#print(removed_spaces)

### Eliminate date stamps ###
date_format = "%B %d, %Y"
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#day = list(range(1, 32))

def eliminate_dates(removed_spaces):
    removed_date_lines = []
    for line in removed_spaces:
        # This is not ideal since it removes any line that starts with a month
        # See if I can program this later to make it specific for each day
        if any (line.startswith(m) for m in month):
            pass
        else:
            removed_date_lines.append(line)
    return removed_date_lines

# Save output
eliminated_dates = eliminate_dates(removed_spaces)

# Test
print(eliminated_dates)

### Step 2: Formatting Chapter Titles ###
#def format_page_numbers(eliminate_dates):

# Delete the page number (denoted by ", p. ") from the end of the chapter title line and appends it to the end of the next line
#a Not all chapter titles have this so I'll need to account for that (it shoudl be accounted for anyway)
## So chapter titles become duplicates and notes have accurate page numbers 
## Removes duplicate lines 
            # https://www.geeksforgeeks.org/python-list-remove/
            # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
            # https://careerkarma.com/blog/python-remove-duplicates-from-list/#:~:text=There%20are%20a%20couple%20of,you%20have%20into%20a%20set.
    # Identify which lines are duplicates and switch them to h2
    #fn.write("<h2>" + line + "</h2>")
# Delete duplicate lines but leave the first instance of each duplicate



        #Add line that drives people back to my website/twitter/youtube (my CTA)


### Step x: Export to HTML file ###

with open('formatted_notes.html', 'w') as fn:
    for line in eliminated_dates:
        print(line, file=fn)