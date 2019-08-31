'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(my_string):

    length = len(my_string)
    if length == 0 or length < 2:
        return 0
    if my_string[0: 2] == 'th':
        return count_th(my_string[1:]) + 1
    return count_th(my_string[1:])