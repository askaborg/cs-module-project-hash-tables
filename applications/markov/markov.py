import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
def markov(a):
    cache = {}
    a = " ".join(a.split()).split(" ")
    prev_word = ""

    for word in a:
        word = word.strip('()"}{')
        if cache.get(f"{word}"):
            cache[prev_word].append(word) 
        else:
            cache[word] = []
            if len(prev_word) > 0:
                cache[prev_word].append(word)
        prev_word = word
    keys = list(cache.keys())
    random.shuffle(keys)
    sentence = []
    word_count = 0
    new_word = ""
    for word in keys: 
        if word_count == 0 and word[0]:
            sentence.append(f"{word}")
            word_count += 1
            new_word = random.choice(cache[word])
            break
    while cache[new_word] != []:              
            new_word = random.choice(cache[new_word])
            sentence.append(f"{new_word}")
            word_count += 1
            if new_word[-1] in list(["." ,"?" ,"!"]):
                return (" ".join(sentence))

# TODO: construct 5 random sentences
# Your code here
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
