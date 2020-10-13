'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Take a string and check for letter combination
# Base case stops when there are no more letters
# If there are letters check if letter combo matches
# If letter combo matches add one number to the count
# Move to the next letter and check for that combo
# If the letters don't match move to next set of letters
# Remove one letter from the string with every check

def count_th(word):
    # Set base case to <= 1 because if string is only 1 character long it is not a match    
    if len(word) <= 1:
        # Return 0 because there are no matching characters
        return 0
    # If the string is longer than 1 charcater check for match
    else:
        # Set count to 0
        count = 0
        # Check if the first two characters = th. If match, add 1 to count
        if word[0:2] == 'th':
            count = 1
        # Return the current count and then run the function again minus the first character
        return count + count_th(word[1:])
 