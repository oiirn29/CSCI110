#Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — 
#perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
#Write a function which removes all punctuation from the string, breaks the string into a list of words, 
#and counts the number of words in your text that contain the letter “e”. 
#Your program should print an analysis of the text like this:

#Your text contains 243 words, of which 109 (44.8%) contain an "e".

import string           #imports the string librariy 

#fisrt vererse from the song "hurry hurry" by air traffic controller
text= '''I wish I'd snoozed, 
I could have used a bit more sleep!
Put on my shoes these ones
are ruining my feet.
Eat that apple to the core
as I hurry hurry out the door!'''

def remove_punctuation(s):          #def that makes a function that remove all the punctuation

    s_without_punct = ""        #veriable deffines strings 

    for letter in s:        #for loop that goes through the s veriable and remove all the punctuations from the strings 
        
        if letter not in string.punctuation:            #if loop that uses the string libbrry we added in and the .punctuation 

            s_without_punct += letter

    return s_without_punct

out = remove_punctuation(text).split()      #creates veriable that uses the remove_punctuation, 
                                            #and the .split function that devides the lagre string into strings by word

total_amount = len(out)     #veriable that uses the len output to count the amount of strings present after the .split

letter = "e"          #deffines the letter e

words_with_letter = sum(1 for word in 
                            out 
                            if letter in word)            #veriable that deffines a for loop that checks for "e"   

if total_amount > 0:

    pain = (words_with_letter * 100) / total_amount

    print(f'Your text contains {total_amount} words, of which {words_with_letter} ({pain}%) contain an "e".')


