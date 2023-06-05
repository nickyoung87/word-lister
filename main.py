import re

print('What file would you like to load the text from?')
read_from_file = input()

print('What file would you like to save the word list to?')
save_to_file = input()

print('Append to or overwrite the save file? [a = append, w = overwrite (default)]')
new_file_flag = input()

if ( new_file_flag != 'a' or new_file_flag != 'w'):
    new_file_flag = 'w'

print('Do you want to remove puncuation from the words? [y = yes (default), n = no)]')
remove_punctuation = input()

if ( remove_punctuation != 'y' or remove_punctuation != 'n'):
    remove_punctuation = 'y'

print('What word length do you want to filter out?')
word_length = int(input())

new_file = open(save_to_file, new_file_flag)

with open(read_from_file,'r', encoding="utf8") as f:
    for line in f:
        for word in line.split():
           
           escaped_word = word

           # Remove punctuation
           if(remove_punctuation == 'y'):
              escaped_word = re.sub(r'[^\w\s]', '', word)

           if(len(escaped_word) > word_length):
              new_file.write(escaped_word)
              new_file.write("\n")

new_file.close()