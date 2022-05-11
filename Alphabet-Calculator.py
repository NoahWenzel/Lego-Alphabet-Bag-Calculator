import static_variables as svar
import pprint
import math
import regex


phrase = '''
Input Phrase Here!!!!!!!
'''
# Strip out all spaces, special characters and numbers, then make all upper case.
phrase = regex.sub('[^A-Za-z]+', '', phrase).upper()
phrase_breakdown = svar.phrase_breakdown
bags_needed = 0

# Figure out the breakdown of the phrase 
for letter in phrase:
    if letter == 'M' or letter == 'W':
        phrase_breakdown['W'] += 1
    else:
        phrase_breakdown[letter] += 1

pprint.pprint(phrase_breakdown)

# Compare the phrase_breakdown to what a bag has to find out how many bags are needed
for letter in svar.bag:
    num = math.ceil(phrase_breakdown[letter] / svar.bag[letter])

    if num > bags_needed:
        bags_needed = num

print(bags_needed)