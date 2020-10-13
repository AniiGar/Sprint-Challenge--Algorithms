def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]

selection_sort([0,2,34,22,10,19,17])

"""
- Start at [0] and hold that number
- Move right and comppare the number value to the held number
    - If the number value is equal or higher move right. Move right again and compare the next number.
    - If the number to the right is lesser than the held number, swap the held number with the lesser numbers position. Move right again and compare the next number.
- If at the end of the list, move left until you can't move left and start the sort again. 
- If there are are no swaps in a pass, end the sort. 


Old thought process...

Selection sort seems the best way to complete this task.

Start at [0] and hold the number. 
Move left and compare each number until you reach a number that is lower than the held number.
Mark that number as lower number and continue to check the rest of the list.
If another lower number, mark that number.
Swap the held number with the marked lower number.
Go back to the begining of the list, plus one space.
Continue the swap process again. 
"""