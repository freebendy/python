def letterCount(str):
    letterCounts = {}
    for letter in str:
        letterCounts[letter]=letterCounts.get(letter,0)+1
    return letterCounts