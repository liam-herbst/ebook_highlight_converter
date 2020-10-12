import os
ibook_highlighter_converter = os.path.dirname(os.path.abspath(__file__))
my_file = open(os.path.join(ibook_highlighter_converter, 'ex_notes.txt'))

print(my_file.readlines())