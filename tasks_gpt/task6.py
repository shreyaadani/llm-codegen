import re

def longest_word(sentence):
    # take only alphanumeric runs as words
    words = re.findall(r"[A-Za-z0-9]+", sentence)
    if not words:
        return ""
    maxlen = max(len(w) for w in words)
    # return the first word with max length (stable tie-break)
    for w in words:
        if len(w) == maxlen:
            return w
