#-------------------------------------------------------------------------------
# Name:        20.8 exercise 3
# Purpose:   alphabeticaly list all words and the amount of times they occur in the book Alice’s Adventures in Wonderland.
#
# Author: Joshua Mazurak
#
# Created:11/3/2024
# Licence: CC BY
#-------------------------------------------------------------------------------


#Write a program called alice_words.py that creates a text file named alice_words.txt 
# containing an alphabetical listing of all the words, and the number of times each occurs, 
# in the text version of Alice’s Adventures in Wonderland. 
# (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) 
# The first 10 lines of your output file should look something like this:
# Word              Count
# =======================
# a                 631
# a-piece           1
# abide             1
# able              1
# about             94
# above             3
# absence           1
# absurd            2


punctuation = "!\"“#$%&'()’‘*+,./:;<=>?@[\\]^_`{|}~”1234567890"       #list of strings to exclude 

def remove_punctuation(s):          #removes the strings listed in "punctuation"
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct

file = open("alices_adventures_in_wonderland.txt", encoding='utf-8')        #opens the Alice’s Adventures in Wonderland. file in utf-8 
text = file.read()        #reads the contents and assinges them to var      #the copy paste format from gutenberg is in utf-8 = pain
file.close()            #closes file 

all_words = remove_punctuation(text).lower().replace("-", " ").replace("—", " ").split()        
#takes var text removes all the punctuation lowers all the 
#cappital letters removes the hpyons and dashes then splits this strings up. this book as some weird punctuation btw

word_count = {}             #var of how many words 

for words in all_words:             #finds all the same type of words and tallies the amount 
    word_count[words] = word_count.get(words, 0)+1

word_items = list(word_count.items())       #sorts all the strings 
word_items.sort()

file_output = open("Alice_words.txt", "w")          #opens a new txt file for the output 

file_output.write("Word              Count\n=======================\n")     #creates the hedder 
for word, occurrences in word_items:
    file_output.write(f"{word:<18}{occurrences}\n")         #writes all the lines out in a f-string format 

file_output.close()         #closes the new file 
