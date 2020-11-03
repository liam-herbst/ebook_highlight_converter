# --------------------------------------------------
# STEP 1: PASTE YOUR HIGHLIGHTS INTO THE 'PASTE_HIGHLIGHTS_HERE.TXT' FILE
# STEP 2: SAVE THE 'PASTE_HIGHLIGHTS_HERE.TXT' FILE
# STEP 3: RUN THIS SCRIPT
# STEP 4: GO TO '[YOUR BOOK & YOUR BOOK AUTHOR].HTML AND SAVE YOUR FILE
# STEP 5: IMPORT YOUR FILE INTO NOTION (CLICK HTML FILE)
# --------------------------------------------------

### Import modules and files ###

from datetime import datetime
#from collections import Counter [may need to import later]
import sys
import os

original_notes = 'paste_highlights_here.txt'
#print(original_notes)

with open(original_notes, 'r') as original_notes:
    og_original_lines = original_notes.readlines()
    original_lines = og_original_lines[3:]

# Confirm highlights properly converted to a list
#print(type(original_lines))

# Confirm highlights properly outputted
#print(original_lines)

### Format Import ### 

# Delete line break at end of list objects
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
print(removed_spaces)

# Delete the page number (denoted by ", p. ") from the end of the chapter title line and append it to the note line
## + Convert chapter titles into headers and highlights/notes into bullets
def format_lines(removed_spaces):
    formattedlines = []
    l = -1
    location = ''
    for line in removed_spaces:
        # Format first line as header (it's always a section head)
        if line == removed_spaces[0]:
            formattedlines.append('<h2>' + line + '</h2>')
        elif line.startswith('Highlight(') and (line.find(' Location ') - line.find(')')) < 5 and hasattr(' Page ', line) == False:
            print('shaba shaba')
        elif line.startswith('Highlight(') and (line.find(' Location ') - line.find(')')) < 10 and hasattr(' Page ', line) == True:
            print('hubba hubba')
        # Format chapter headings for headings with Page #s
        elif line.startswith('Highlight(') and hasattr(' Page ', line) == True:
            h = line.find(')')
            p = line[' Page ']
            l = line.find(' Location ')
            formattedlines.append('<h2>' + line[h+4:p] + '</h2>')
        # Format chapter headings (no page #)
        elif line.startswith('Highlight('):
            h = line.find(')')
            l = line.find(' Location ')
            location = "[Loc. " + line[l+10:] + ']'
            formattedlines.append('<h2>' + line[h+4:l] + '</h2>')
        ## Option for if there are no page numbers with the original title lines
        elif formattedlines[-1].startswith('<h2>') and l >= 0:
            formattedlines.append('<ul><li>' + line + location + '</li></ul>')
        # Format highlights
        elif formattedlines[-1].startswith('<h2>') and l < 0:
            formattedlines.append('<ul><li>' + line + '</li></ul>')
        # Format notes
        elif formattedlines[-1].startswith('<ul><li>') >= 0 or formattedlines[-1].find(line) >= 0:
            formattedlines.append('<p><b>Note: </b>' + line + '</p>')
        else:
            pass
    return formattedlines

# Save output
formatted_lines = format_lines(removed_spaces)

# Test
#print(formatted_lines)


### Export to HTML file ###

# Format Title
unmodified_title = og_original_lines[1]
title = unmodified_title[:-1]

# Format Author
unmodified_author = og_original_lines[2]
author = unmodified_author[:-1]

#Format file for creation and write
export_file_name = (title + ' by ' + author)

#export_file = "%s.html" % export_file_name
export_file = export_file_name + '.html'

# Test
#print(export_file)

with open(export_file, 'w') as fn:
    fn.write('\n'.join(formatted_lines))