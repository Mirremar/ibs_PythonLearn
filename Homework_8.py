import os

with open('Homework_8_source.txt','r') as f:
    chars = f.read()
chars_reversed = chars[::-1]
with open('Homework_8_destination.txt','w') as f:
    f.write(chars_reversed)