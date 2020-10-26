### The place for code I previously tested and wanted to archive

import sys

#with open("ex_notes.txt", "r") as en:
 #   print(ex_notes)



 ### Link the old notes file to this script ###
#ibook_highlighter_converter = os.path.dirname(os.path.abspath(__file__))
#old_notes = open(os.path.join(ibook_highlighter_converter, 'ex_notes.txt'))

string = "aositn aoitnea \n"

def test():
    if string[:-2] == '\n':
        return 'hell ya'
print(test())


# Identify dates as strings
        #if line.format(datetime.strftime(line, date_format)):
        #    eliminate_dates.append(line)
#print(eliminate_dates(old_lines))
# no_date_lines = [line for line in old_lines if line == datetime.strptime(line, date_format)]
#newer_lines = old_lines.remove(line == date_format)
#print(newer_lines)



 #for count in reversed(range(len(formatted_page_numbers))):
        #line = formatted_page_numbers[count]
        #if line in counts and counts[line]:
            #line = "<h2>" + line + "</h2>"
        #else:
            #line = "- " + line
    #return formatted_page_numbers


    if num > 1:
            for h2 in range(0, num + 1):
                formatted_page_numbers[formatted_page_numbers.index(s)] = "hellllloooooo"
        else:
            pass

# Count existing chapter title
counts = {line:count for line,count in Counter(formatted_page_numbers).items() if count > 1}

# Test
print(counts)
print(counts.items)

# Convert chapter titles into headers and highlights/notes into bullets
def format_lines(formatted_page_numbers):
    formatted_list = []
    for i,v in enumerate(formatted_page_numbers):
        totalcount = formatted_page_numbers.count(v)
        count = formatted_page_numbers[:i].count(v)
        formatted_list.append(v + str("<h2>") if totalcount > 1 else v)
    return formatted_list