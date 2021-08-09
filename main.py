def translator(lang):
    if lang == 'en':
        return 'English'
    elif lang == 'ba':
        print('Bangla')
    else: print('Hello World!')

e = 'en'
b = 'ba'
print(translator(e),'language')