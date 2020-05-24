# user input
text = input("Please input a line of text: ")

# making string into list 
words = text.split()

# forloop to translate sentence into pig latin 
pig_latin = ""
for word in words:     
    if word[0] in ["a", "e", "i", "o", "u"]: 
        new_word = word + "way"
        pig_latin = pig_latin + " " + new_word
    else:
        # find first instance of a vowel
        for index, letters in enumerate(word):
            if letters in ["a", "e", "i", "o", "u"]:
                first_vowel = index
                #break at the first instance of a vowel instead of all instances for the word
                break        
        new_word = word[index:] + word[:index] + "ay"
        pig_latin = pig_latin + " " + new_word

print("The sentence in Pig Latin is:" + str(pig_latin))