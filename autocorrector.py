from autocorrector import Speller 

corrector = Speller(lang="es")

def correct_word(word):

    if not corrector(word) == word:
        return corrector(word)
    else:
        return word
    print(correct_word("me guzta los ejersisios"))