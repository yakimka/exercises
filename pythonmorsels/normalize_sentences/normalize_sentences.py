import re


def normalize_sentences(sentence):
    return re.sub(r'([^.].[.?!]) +', r'\1  ', sentence)
