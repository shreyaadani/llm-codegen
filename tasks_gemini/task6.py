def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    
    # Define a key function to calculate the "effective" length by counting only alphabetic characters
    def effective_len(word):
        return sum(1 for char in word if char.isalpha())

    # Find the word from the original list that has the maximum effective length
    return max(words, key=effective_len)