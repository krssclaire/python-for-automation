# MAD LIBS
from pathlib import Path

editable_words = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN']

# user input
def get_user_inputs(inputs):
    user_inputs = [] #['silly', 'chandelier', 'screamed', 'pickup truck']        # to edit after testing
    
    for i in range(len(inputs)):
        if inputs[i][0] == 'A':
            print(f'Enter an {inputs[i]}: '.capitalize())
        else:
            print(f'Enter a {inputs[i]}: '.capitalize())
        user_inputs.append(input())
    
    print(user_inputs)
    return user_inputs

user_inputs = get_user_inputs(editable_words)

# edit file
def substitute_text(target_file, target_words, output_words):
    BASE_DIR = Path(__file__).resolve().parent
    path = BASE_DIR / target_file
    content = path.read_text(encoding='utf-8')

    for i in range(len(target_words)):
        content = content.replace(target_words[i], output_words[i], 1)

    new_path = BASE_DIR / f'./outputs/new-{target_file}'
    new_path.write_text(content, encoding='utf-8')

    print(content)
    return content

substitute_text('spam.txt', editable_words, user_inputs)