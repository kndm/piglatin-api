from string import punctuation
from re import split, search, sub

_VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
_PUNCTUATION = set(punctuation)

def _convert_word(word):
    """
    Translate the word using.
    Assuming that it can only be letters.

    Args: word -> Word to translate. ONLY LETTERS ALLOWED.
    Returns: string -> Translated word.

    """

    if not isinstance(word, basestring):
        raise TypeError('_convert_word(): Arg must be a string.')

    first_vowel = -1
    for i in range(len(word)):
        if word[i] in _VOWELS:
            first_vowel = i
            break

    if first_vowel == -1:
        converted_word = word + 'ay'
    elif first_vowel == 0:
        converted_word = word + 'yay'
    else:
        converted_word = word[first_vowel:] + word[:first_vowel] + 'ay'

    return _fix_title_case(converted_word, word)

def _split_words(text):
    if not isinstance(text, basestring):
        raise TypeError('_split_words(): Arg must be a string.')

    return split('(\s+)', text)

def _join_words(words):
    """
    Recombine word-tokenized text into strings.

    Args: words -> words to recombine

    Returns: string -> recombined text

    """

    if type(words) not in [list, tuple]:
        raise TypeError('_join_words(): Argument must be a list or a tuple')
    elif len(words) == 0:
        raise ValueError('_join_words(): Argument must have at least one element')

    return ''.join(words)

def _trim_punctuation(word):
    """
    Trim punctuation from the beginning or end of a word.
    Preserves contractions with punctuation in the middle of the word.

    Args: word -> word to trim

    Returns: string -> the word without leading or trailing punctuation
    """

    if not isinstance(word, basestring):
        raise TypeError('_trim_punctuation(): Argument must be a string.')

    return word.strip(''.join(_PUNCTUATION))

def _fix_title_case(word, match_word):
    """
    Match pig latin translation to capitalization of original word if it was title case

    Args: word -> word to change , match_word -> word to match

    Returns: string -> word with capitalization fixed if needed
    """

    match_word = sub('[^a-zA-Z]', '', match_word)
    if match_word.istitle():
        return word[0].upper() + word[1:].lower()
    return word
