from os import linesep
from re import search
from src.helpers import _convert_word, _split_words, _trim_punctuation, _fix_title_case, _join_words

def to_pig_latin(text):
    """
    Convert text to pig latin
    Args: text -- Text to convert 
    
    """
    
    if not isinstance(text, basestring):
        raise TypeError('to_pig_latin(): Arg must be a string.')

    converted_words = []
    for word in _split_words(text):
        if not search('[a-zA-Z]', word):
            converted_words.append(word)
            continue

        trimmed_word = _trim_punctuation(word)
        if len(trimmed_word) == 0:
            converted_words.append(word)
            continue

        converted_word = word.replace(trimmed_word, _convert_word(trimmed_word))
        converted_words.append(converted_word)

    return _join_words(converted_words)
