####Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

###Strings passed in will consist of only letters and spaces.
###Spaces will be included only when more than one word is present.

def split_sentence(sentence):
    sentence_list=sentence.split()
    return sentence_list

word_list=split_sentence('thiseee ise ae testte e eee dd')    

def spin_words(words):
    word_len=len(words)
    if word_len >= 5: 
        word_spin=words[::-1]
    else:
        word_spin=words
    return word_spin

spin_words_list=list(map(spin_words,word_list))

print(" ".join(str(i) for i in spin_words_list))
