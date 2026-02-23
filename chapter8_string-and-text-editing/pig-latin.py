# PIG LATIN 

print('Enter the English message to translate into Pig Latin')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u')

pig_latin = []
for word in message.split():
    # separate non-letters at the start of this word
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # separate non-letters at the end of this word
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]
        
    # remember if the word was uppercase or capitalized
    was_upper = word.isupper()
    was_title = word.istitle()
    
    # make the word lowercase for translation
    word = word.lower()

    #separate the consonants at the start of the word
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # add pig latin ending
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else: 
        word += 'yay'

    # set the word back to uppercase or capitalized
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # add non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# join all words back together
print(' '.join(pig_latin))