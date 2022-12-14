from functools import wraps
from string import punctuation

from django.core.exceptions import ValidationError


def validate_perfect(*must_words):
    @wraps(validate_perfect)
    def validate_wrapped(value):
        clean_value = clean_text(value, punctuation)
        words_in_value = list(map(lambda word: word.lower(),
                                  clean_value.split()))
        for elem in must_words:
            if elem.lower() in words_in_value:
                return
        words = ', '.join(must_words)
        raise ValidationError(f'Обязательно используйте {words}')
    return validate_wrapped


def clean_text(text, symbols):
    clean_text = ''
    for symb in text:
        if symb not in symbols:
            clean_text += symb
        else:
            clean_text += ' '
    return clean_text
