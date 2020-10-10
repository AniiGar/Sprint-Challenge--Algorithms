'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):

#     if not word:
#         return 0
#     elif word[0]==th:
#         return 1+count_th(word[1:])
#     else:
#         return count_th(word[1:])
    
    # count = 0
  
    # for i in test_str: 
    #     if i == 'e': 
    #         count = count + 1
    

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
# string=raw_input("Enter string:")
# ch=raw_input("Enter character to check:")
print("Count is:")
print(check('dnvlajdlch chch adlfljlajch', 'ch'))