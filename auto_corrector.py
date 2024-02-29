from autocorrect import Speller 

corrector = Speller(lang="es")

def correct_word(word):

    if not corrector(word) == word:
        return corrector(word)
    else:
        return word
    print(correct_word("lo boy a intentar"))