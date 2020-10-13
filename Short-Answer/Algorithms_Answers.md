#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This snippet is O(n) because the n cancels out to 1n and the constant is dropped.


b) This snippet is O(n2) because it is a nested loop. Every time this code is executed the runtime complexity is exponentiated. 


c) This snippet is O(n) because bunnies is equivalent to n. It is being called n times before it reaches the base case. 

## Exercise II

A binary search would be the best way to find the right floor with the least eggs dropped and broken. Its runtime complexity is O(log n)

Go to the middle and drop and egg. 

If the egg does not break:
    The next higher floor is the starting point. And the top floor is still the highest floor. Go to the middle floor between those two and drop another egg. Continue this pattern until you find the floor that the egg breaks on, that is floor f.

If the egg breaks:
    The next floor lower is the ending floor. And the first floor is still the lowest floor. Go to the middle floor between those two and drop another egg. Continue this pattern until you find the floor that the egg does not break on, the floor that is one higher is floor f.

