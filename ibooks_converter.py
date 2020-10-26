#See if it's possible to modify the file name to reflect the book
## E.g. Formatted: Almanack of Naval
#Ideally I'll be able to automatically make a bulleted list for the notes under each chapter 
#for the time being I could just add a "- " for each item so I can input that way into notion

### Import modules and files ###

from datetime import datetime
import sys
import os

with open('ex_notes.txt', 'r') as original_notes:
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


# Identify chapter titles (duplicate lines) and convert them into headers (convert highlights and notes into bullets)
#def format_lines(formatted_page_numbers):
 # Identify which lines are duplicates and switch them to h2
    #fn.write("<h2>" + line + "</h2>")
# Delete duplicate lines but leave the first instance of each duplicate

# Save output
#formatted_lines = format_lines(formatted_page_numbers)

# Test
#print(formatted_lines)

# Remove duplicate chapter titles
def remove_chapter_duplicates(formatted_lines):
    remove_ch_dup = []
    for line in formatted_page_numbers:
        if line not in remove_ch_dup:
            remove_ch_dup.append(line)
        else:
            pass
    return remove_ch_dup

# Save output
removed_chapter_duplicates = remove_chapter_duplicates(formatted_page_numbers)

# Test
print(removed_chapter_duplicates)

#Add line that drives people back to my website/twitter/youtube (my CTA)

### Export to HTML file ###

with open('test.html', 'w') as fn:
    for line in removed_chapter_duplicates:
        fn.write(line)