# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import string

with open("./ciphertext.txt") as coder:
    coder = coder.read()
encode_char = set(string.ascii_uppercase)
freq = {}
letter_count = 0

for char in coder:
    if char in encode_char:
        letter_count += 1
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

freq_ranked_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
frequency = [(letter, freq[letter]) for letter in freq]
frequency.sort(key=lambda tup: tup[1], reverse=True)
decoder = {frequency[i][0]: letter for (i, letter) in enumerate(freq_ranked_letters)}
decoded_text = ''

for char in coder:
  if char not in encode_char:
    decoded_text += char
  else:
    decoded_char = decoder[char]
    decoded_text += decoded_char

print(decoded_text)
