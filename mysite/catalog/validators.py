from django.core.exceptions import ValidationError


def validate_perfect(value):
    must_words = ['роскошно', 'превосходно']
    clean_value = clean_text(value, ('!', ',', '?', '.'))
    words_in_value = list(map(lambda word: word.lower(), clean_value.split()))
    for elem in must_words:
        if elem.lower() in words_in_value:
            return
    words = ', '.join(must_words)
    raise ValidationError(f'Обязательно используйте {words}')


def clean_text(text, symbols):
    clean_text = ''
    for symb in text:
        if symb not in symbols:
            clean_text += symb
    return clean_text
