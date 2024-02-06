#!/usr/bin/python3
'''
function that print all elements
'''


class MyList(list):
    '''subclass of list '''
    def print_sorted(self):
        '''prints sorted list'''
        print(sorted(self))
