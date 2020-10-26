# --------------------------------------------------
# STEP 1: PASTE YOUR NOTES INTO THE 'UNFORMATTED_HIGHLIGHTS.TXT' FILE
# STEP 2: SAVE THE 'UNFORMATTED_HIGHLIGHTS.TXT' FILE
# STEP 3: RUN THIS SCRIPT
# STEP 4: GO TO 'FORMATTED_HIGHLIGHTS.TXT AND SAVE YOUR FILE
# STEP 5: IMPORT YOUR FILE INTO NOTION (CLICK HTML FILE)
# --------------------------------------------------

### Import modules and files ###

from datetime import datetime
from collections import Counter
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
#print(eliminated_dates)

### Formatting Chapter Titles ###

# Delete the page number (denoted by ", p. ") from the end of the chapter title line
## Ideally, the page number would append to the next highlight but hey... This isn't bad 
def format_page_numbers(eliminated_dates):
    formatted_pg_num = []
    for line in eliminated_dates:
        if line.find(", p. ") >= 0:
            a = line.find(", p. ")
            formatted_pg_num.append(line[:a])
        else:
            formatted_pg_num.append(line)
    return formatted_pg_num

# Save output
formatted_page_numbers = format_page_numbers(eliminated_dates)

# Test
#print(formatted_page_numbers)

# Convert chapter titles into headers and highlights/notes into bullets
def format_lines(formatted_page_numbers):
    formatted_lines = []
    for line in formatted_page_numbers:
        if formatted_page_numbers.count(line) > 1:
            line = '<h2>' + line + '</h2>'
            formatted_lines.append(line)
        else:
            line = '<p>- ' + line + '</p>'
            formatted_lines.append(line)
    return formatted_lines

# Save output
formatted_lines = format_lines(formatted_page_numbers)

# Test
#print(formatted_lines)

# Remove duplicate chapter titles
def remove_chapter_duplicates(formatted_lines):
    remove_ch_dup = []
    for line in formatted_lines:
        if line not in remove_ch_dup:
            remove_ch_dup.append(line)
        else:
            pass
    return remove_ch_dup

# Save output
removed_chapter_duplicates = remove_chapter_duplicates(formatted_lines)

# Add line for users to connect with me
#removed_chapter_duplicates.append("Thanks for using this script converter. If you have any questions or would like to stay up to date on new things I'm building,you can follow me on twitter @liamherbst29")

# Test
print(removed_chapter_duplicates)

### Export to HTML file ###

with open('formatted_highlights.txt', 'w') as fn:
    fn.write('\n'.join(removed_chapter_duplicates))