from googletrans import Translator
translator = Translator()

translate_channel = translator.translate('Suresh Arunachalam', src='en', dest='ta')
print(translate_channel)