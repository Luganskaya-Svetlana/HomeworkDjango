from django.core.exceptions import ValidationError


def validate_perfect(value):
    must_words = ['роскошно', 'превосходно']
    for elem in must_words:
        if elem.lower() in value.lower():
            return
    words = ', '.join(must_words)
    raise ValidationError(f'Обязательно используйте {words}')
