# --------------------------------------------------
# STEP 1: PASTE YOUR HIGHLIGHTS INTO THE 'UNFORMATTED_HIGHLIGHTS.TXT' FILE
# STEP 2: SAVE THE 'UNFORMATTED_HIGHLIGHTS.TXT' FILE
# STEP 3: RUN THIS SCRIPT
# STEP 4: GO TO 'FORMATTED_HIGHLIGHTS.TXT AND SAVE YOUR FILE
# STEP 5: IMPORT YOUR FILE INTO NOTION (CLICK HTML FILE)
# --------------------------------------------------

### Import modules and files ###

from datetime import datetime
#from collections import Counter [may need to import later]
import sys
import os

original_notes = 'unformatted_highlights.txt'
print(original_notes)

with open(original_notes, 'r') as original_notes:
    original_lines = original_notes.readlines()

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
#print(removed_spaces)

### Eliminate date stamps ###
### Eliminate date stamps ###

date_format = '%B %d, %Y'
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
#print(eliminated_dates)

### Formatting Lines ###

# Delete the page number (denoted by ", p. ") from the end of the chapter title line and append it to the note line
def format_page_numbers(eliminated_dates):
    formatted_pg_num = []
    # e is the page # and note variable
    e = ''
    for line in eliminated_dates:
        # Account for if the user copies in the ending lines from the original email import
        if line.find('All Excerpts From') >= 0:
            e = ""
            formatted_pg_num.append('<p>' + line + '</p>')
        # If page number is in the line (i.e. it's a chapter), delete it from the line and store the page number as e
        elif line.find(', p. ') >= 0:
            a = line.find(', p. ')
            e = line[a:]
            e = ' [' + e[2:] + ']'
            formatted_pg_num.append('<h2>' + line[:a] + '</h2>')
        # If page number is not in the line (i.e. it's a highlight), append it to the line
        ## Change e to e = "Note: " because if there are two or more consecutive lines without ", p. ", the lines after line 1 are notes
        elif line.find(', p. ') < 0 and e.find('[') >= 0:
            formatted_pg_num.append('<ul><li>' + line + e + '</li></ul>')
            e = '<b>Note:</b> '
        # Add "Note: " to the beginning of the note line
        elif e == '<b>Note:</b> ':
            formatted_pg_num.append('<ul><li>' + e + line + '</li></ul>')
        # Account for lines that preceed the first chapter highlight instance
        else:
            formatted_pg_num.append('<p>' + line + '</p>')
    return formatted_pg_num

# Save output
formatted_page_numbers = format_page_numbers(eliminated_dates)

# Test
print(formatted_page_numbers)

# Remove duplicate chapter titles
def remove_chapter_duplicates(formatted_page_numbers):
    remove_ch_dup = []
    for line in formatted_page_numbers:
        if line not in remove_ch_dup:
            remove_ch_dup.append(line)
        else:
            pass
    return remove_ch_dup

# Save output
removed_chapter_duplicates = remove_chapter_duplicates(formatted_page_numbers)

# Add line for users to connect with me
#removed_chapter_duplicates.append("Thanks for using this script converter. If you have any questions or would like to stay up to date on new things I'm building,you can follow me on twitter @liamherbst29")

# Test
print(removed_chapter_duplicates)

### Export to HTML file ###

with open('formatted_highlights.html', 'w') as fn:
    fn.write('\n'.join(removed_chapter_duplicates))