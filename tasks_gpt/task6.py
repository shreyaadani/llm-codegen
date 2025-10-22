def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)
