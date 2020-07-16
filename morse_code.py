'''
You are given a dictionary that maps letters and digits to Morse code. Write a function named translate_into_morse() that 
takes a string as an input parameter and returns its Morse representation. If a given character is not available in the dictionary, return it "as it is". 
Don't forget to uppercase the input string to match our morse dictionary! 
'''

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--'}

# def translate_into_morse(string):
    
#     output = ''
#     for key in morse.keys():
#         for letter in string:  
#             if letter.upper() == key:
#                 output += morse[key]
#     return output
   

def translate_into_morse(string):
  string=string.upper()
  text=''
  for word in string:
    for key in word: 
      if key in morse.keys():
        text = text + morse[key]
      else:
        text = text + key
  return text
   

# print(translate_into_morse("aS IS COOL"))
#print(translate_into_morse("MORSE CODE IS COOL"))
translate_into_morse('MORSE CODE IS COOL')