sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:

    if word in frequency:

        frequency[word] = frequency[word] + 1

    else:

        frequency.update({word: 1})

print("Word frequency:", frequency)

print("Unique words:")

for key in frequency:

    print(key)

print("Total unique words:", len(frequency))

max_count = 0

for key, value in frequency.items():

    if value > max_count:

        max_count = value

        max_word = key

print("Most frequent word:", max_word, max_count)

min_count = float('inf')

for key, value in frequency.items():

    if value < min_count:

        min_count = value

        min_word = key

print("Least frequent word:", min_word, min_count)

sorted_frequency = {}

for key in sorted(frequency):
    
    sorted_frequency.update({key: frequency[key]})

print("Alphabetical order:", sorted_frequency)
