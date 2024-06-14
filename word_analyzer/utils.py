# utils.py
def count_vowels(words):
    vowel_counts = {
        word: sum(1 for char in word if char in 'aeiouAEIOU') for word in words
    }
    return vowel_counts


def sort_words(words, order):
    return sorted(words, reverse=(order == 'desc'))
