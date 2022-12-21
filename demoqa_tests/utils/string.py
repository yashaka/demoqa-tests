import re


def is_word_with_dashes_underscores_or_numbers(text):
    return re.match(r'^[a-zA-Z_\d\-]+$', text)
