"""
Problem 5
20.0/20.0 points (graded)
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.

Here are some examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

Code Editor
1
# Paste your function here
"""
def dict_invert(d):

    inverse = {}
    for element in d.keys():
        if d[element] in inverse:
            inverse[d[element]].append(element)
        else:
            inverse[d[element]] = [element]
    for val in inverse.values():
        val.sort()
    return inverse