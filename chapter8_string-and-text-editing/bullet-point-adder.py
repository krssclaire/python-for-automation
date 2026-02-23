import pyperclip

pyperclip.copy('Lists of animals\nLists of aquarium life \nLists of biologists by author abbreviation \nLists of cultivars')
text = pyperclip.paste()

lines = text.split('\n')
new_text = ''

for i in range(len(lines)):
    lines[i] = '* ' + lines[i] 

text = '\n'.join(lines)

print(lines)
print(text)
pyperclip.copy(text)