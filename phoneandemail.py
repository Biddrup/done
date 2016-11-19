#! python3
# Finds phone numbers and email addresses on the clipboard.
#Here, p = phone and e = email
#Cope the paragrapgh by using Ctrl+c and the press F5
#Next, will show the result
import pyperclip, re

p = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)', re.VERBOSE)

# Create email regex.
e = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in p.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    matches.append(phonenum)
for groups in e.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Here is your result:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')
