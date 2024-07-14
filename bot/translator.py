from translate import Translator

translator = Translator(to_lang="ru")

def translate_to_russian(text):
    translation = translator.translate(text)
    return translation
