import os

#Organizes the negative results so they can be filtered in the powerline or cmd line level scripts

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir(r'negative'):
            f.write('negative/' + filename + '\n')

print('aaa')

generate_negative_description_file()
