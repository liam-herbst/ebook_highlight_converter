# --------------------------------------------------
# STEP 1: PASTE YOUR BOOK HIGHLIGHTS INTO THE 'PASTE_HIGHLIGHTS_HERE.TXT' FILE
# STEP 2: SAVE THE 'PASTE_HIGHLIGHTS_HERE.TXT' FILE
# STEP 3: RUN THIS SCRIPT
# STEP 4: OPEN YOUR FILE BY SELECTING [YOUR BOOK & YOUR BOOK AUTHOR].HTML IN EBOOK_HIGHLIGHT_CONVERTER FOLDER
# --------------------------------------------------

### Import modules and files ###

from datetime import datetime

original_notes = 'paste_highlights_here.txt'
#print(original_notes)

with open(original_notes, 'r') as original_notes:
    og_original_lines = original_notes.readlines()

def ibook_or_kindle(og_original_lines):
    #################### iBooks ####################
    # I originally posted the iBook notes so I'm leaving them and turning the line into and 'if not' statement instead of re-shifting everything
    if not og_original_lines[0].startswith('Notebook Export'):
        def remove_crap(og_original_lines):
            for line in og_original_lines:
                if line.startswith('NOTES FROM\n'):
                    nf = og_original_lines.index(line)
                    break
                else:
                    continue
            return nf
        nf = remove_crap(og_original_lines)
        original_lines = og_original_lines[nf+3:]

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

        ### Format Lines ###

        #date_format = '%B %d, %Y'

        # Identify dates

        def identify_dates(removed_spaces):
            date_list = []
            for item in removed_spaces:
                try:
                    datetime.strptime(item, '%B %d, %Y')
                    date_list.append(item)
                except ValueError:
                    continue
            return date_list

        dates = identify_dates(removed_spaces)

        # Test
        #print(dates)

        # Delete the page number (denoted by ", p. ") from the end of the chapter title line and append it to the note line
        ## + Convert chapter titles into headers and highlights/notes into bullets
        def format_lines(removed_spaces):
            formattedlines = []
            p = -1
            page = ''
            for line in removed_spaces:
                if line == 'All Excerpts From':
                    break
                elif line in dates:
                    formattedlines.append(line)
                # Format chapter headings
                elif formattedlines[-1] in dates and line not in dates and line.find(', p. ') >= 0:
                    p = line.find(', p. ')
                    page = line[p+2:]
                    formattedlines.append('<h2>' + line[:p] + '</h2>')
                # Account for chapter heading that don't have page numbers
                elif formattedlines[-1] in dates and line not in dates:
                    formattedlines.append('<h2>' + line + '</h2>')
                # Format highlights
                elif formattedlines[-1].startswith('<h2>') and p >= 0:
                    formattedlines.append('<ul><li>' + line + ' [' + page + ']' + '</li></ul>')
                # Option for books without page numbers
                elif formattedlines[-1].startswith('<h2>') and p < 0:
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

        ### Remove lines ###

        # Remove dates and chapter duplicates
        def remove_lines(formatted_lines):
            remove_l = []
            for line in formatted_lines:
                if any (line.startswith(m) for m in dates):
                    pass
                elif line not in remove_l:
                    remove_l.append(line)
                else:
                    pass
            return remove_l

        # Save output
        removed_lines = remove_lines(formatted_lines)

        # Add line for users to connect with me
        #removed_chapter_duplicates.append("Thanks for using this script converter. If you have any questions or would like to stay up to date on new things I'm building,you can follow me on twitter @liamherbst29")

        # Test
        #print(removed_chapter_duplicates)

        ### Export to HTML file ###

        # Format Title
        unmodified_title = og_original_lines[nf+1]
        title = unmodified_title[:-1]

        # Format Author
        unmodified_author = og_original_lines[nf+2]
        author = unmodified_author[:-1]

        #Format file for creation and write
        export_file_name = (title + ' by ' + author)

        #export_file = "%s.html" % export_file_name
        export_file = export_file_name + '.html'

        # Test
        #print(export_file)

        with open(export_file, 'w') as fn:
            fn.write('\n'.join(removed_lines))

    #################### Kindle ####################

    else:
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
        #print(removed_spaces)

        ### Format Lines ###

        # Delete the page number (denoted by ", p. ") from the end of the chapter title line and append it to the note line
        ## + Convert chapter titles into headers and highlights/notes into bullets
        def format_lines(removed_spaces):
            formattedlines = []
            l = -1
            p = -1
            location = ''
            count = -1
            for line in removed_spaces:
                count += 1
                if line == removed_spaces[0]:
                    formattedlines.append('<h2>' + line + '</h2>')
                # Add line to maintain order -- delete in the remove lines section (for lines not including page #s) (<h3> added for consistency)
                elif line.startswith('Highlight(') and (line.find(' Location ') - line.find(')')) < 5:
                    l = line.find(' Location ')
                    l_start = l + 10
                    location = " [" + line[l_start:] + ']'
                    formattedlines.append('<h3>' + line + '***Delete000Later***')
                # Add line to maintain order —- delete in the remove lines section (for lines including page #s)
                elif line.startswith('Highlight(') and (line.find(' Location ') - line.find(')')) < 15 and ' Page ' in line:
                    l = line.find(' Location ')
                    p = line.find(' Page ')
                    p_start = p + 6
                    p_end = l - 2
                    page = ' [p. ' + line[p_start:p_end] + ']' 
                    formattedlines.append('<h3>' + line + '***Delete000Later***')
                # Format chapter headings for headings with Page #s
                elif line.startswith('Highlight(') and ' Page ' in line:
                    l = line.find(' Location ')
                    h = line.find(')')
                    p = line.find(' Page ')
                    p_start = p + 6
                    p_end = l - 2
                    page = ' [p. ' + line[p_start:p_end] + ']'
                    formattedlines.append('<h3>' + line[h+4:p-2] + '</h3>')
                # Format chapter headings (no page #)
                elif line.startswith('Highlight(') and ' Location ' in line:
                    h = line.find(')')
                    l = line.find(' Location ')
                    l_start = l + 10
                    location = " [" + line[l_start:] + ']'
                    formattedlines.append('<h3>' + line[h+4:l] + '</h3>')
                # Format note headings
                elif line.startswith('Note - ') and ' Page ' in line:
                    l = line.find(' Location ')
                    p = line.find(' Page ')
                    p_start = p + 6
                    p_end = l - 2
                    page = ' [p. ' + line[p_start:p_end] + ']'
                    if len(line[7:p-2]) > 0:
                        formattedlines.append('<h3>' + line[7:p-2] + '</h3>')
                    else:
                        pass
                # Format note headings (without pages)
                elif line.startswith('Note - ') and ' Location ' in line:
                    l = line.find(' Location ')
                    l_start = l + 10
                    location = " [" + line[l_start:] + ']'
                    if len(line[7:l]) > 0:
                        formattedlines.append('<h3>' + line[7:l] + '</h3>')
                    else:
                        pass
                # Format notes
                elif removed_spaces[count-1].startswith('Note - ') and ' Page ' in removed_spaces[count-1]:
                    formattedlines.append('<p><b>Note: </b>' + line + page + '</p>')
                elif removed_spaces[count-1].startswith('Note - ') and ' Location ' in removed_spaces[count-1]:
                    formattedlines.append('<p><b>Note: </b>' + line + location + '</p>')
                # Format bookmarks with pages
                elif line.startswith('Bookmark - ') and ' Page ' in line:
                    l = line.find(' Location ')
                    p = line.find(' Page ')
                    p_start = p + 6
                    p_end = l - 2
                    page = ' [p. ' + line[p_start:p_end] + ']'
                    b_page = 'Page ' + line[p_start:p_end]
                    formattedlines.append('<h3>' + line[11:p-2] + '</h3>')
                    formattedlines.append('<b>Bookmark: ' + b_page + '</b>')
                # Format bookmarks without pages
                elif line.startswith('Bookmark - ') and ' Location ' in line:
                    l = line.find(' Location ')
                    l_start = l + 10
                    location = " [" + line[l_start:] + ']'
                    formattedlines.append('<h3>' + line[11:l] + '</h3>')
                    formattedlines.append('<b>Bookmark: ' + location + '</b>')
                # Format highlights with pages
                elif formattedlines[-1].startswith('<h3>') and p >= 0:
                    formattedlines.append('<ul><li>' + line + page + '</li></ul>')
                # Format highlights without pages
                elif formattedlines[-1].startswith('<h3>') and l >= 0:
                    formattedlines.append('<ul><li>' + line + location + '</li></ul>')
                else: # line starts with h2 or ul
                    formattedlines.append('<h2>' + line + '</h2>')
            return formattedlines
        # Save output
        formatted_lines = format_lines(removed_spaces)

        # Test
        #print(formatted_lines)

        ### Remove lines ###

        # Remove chapter duplicates
        def remove_lines(formatted_lines):
            remove_l = []
            for line in formatted_lines:
                if line.endswith('***Delete000Later***'):
                    pass
                elif line not in remove_l:
                    remove_l.append(line)
                else:
                    pass
            return remove_l

        # Save output
        removed_lines = remove_lines(formatted_lines)

        # Add line for users to connect with me
        #removed_chapter_duplicates.append("Thanks for using this script converter. If you have any questions or would like to stay up to date on new things I'm building,you can follow me on twitter @liamherbst29")

        # Test
        #print(removed_lines)

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
            fn.write('\n'.join(removed_lines))

# Call the Function
ibook_or_kindle(og_original_lines)