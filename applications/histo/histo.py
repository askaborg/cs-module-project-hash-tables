# Your code here
with open("./robin.txt") as robin:
    robin = robin.read()

def histo(s):
    if len(s) < 1:
        return {}
    else:
        word_counter = {}
    s = " ".join(s.split()).lower().split(" ")

    for word in s:
        word = word.strip('":;,.-+=/|[]}{()*^&')
        if word_counter.get(f"{word}"):
            word_counter[word] += 1
        else: 
            word_counter[word] = 1
    words = list(word_counter.items())
    words.sort(key=(lambda e: (-e[-1], e[0])))

    for word, a in words:
        word = word + " " * (15-len(word)) + "#" * a
        print(word)

if __name__ == "__main__":
    print(histo(""))
    print(histo(f"{robin}"))
