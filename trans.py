from googletrans import Translator

def text_trans(text,dest):
    try:
        trans = Translator()
        translation = trans.translate(text,dest)
        return translation.text
    except Exception as ex:
        return ex

def original_language(text):
    translator = Translator()
    language = translator.translate(text)
    if language.src == 'en':
        return 'en'
    else:
        return 'ru'
