
# user_input = input('Please provide some text: ')
# word_frequencies = dict()
# word_count = 1
# for word in user_input.split():
#     if word in word_frequencies:
#         word_frequencies[word] = word_count + 1
#     else:
#         word_frequencies[word] = word_count

'''
Write a program that will ask the user for a string value.

Next, create a dictionary named word_frequencies. The dictionary should contain all unique words from the user input as keys, 
and their frequencies (number of occurrences in the string) as values.
'''
user_input = input('Please provide some text: ')

word_frequencies = {}

for word in user_input.split():
    if word in word_frequencies:
        word_frequencies[word] = word_frequencies[word]+1
    else:
        word_frequencies[word] = 1
print(word_frequencies)