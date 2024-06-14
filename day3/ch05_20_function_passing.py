# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:42:25 2024

@author: UD SYSTEMS
"""

"""
    Program: ch05_20_function_passing.py
    Function: Exploring the names of functions
"""

def simple_sort(list_sort, cmp_function):
    new_list_sort = list_sort[:]

    def swap( list_in, a, b ):
        temp = list_in[a]
        list_in[a] = list_in[b]
        list_in[b] = temp
        return
        
        again = True
        while again:
            again = False
            for i in range(0,len(new_list_sort) - 1):
                value = cmp_function(new_list_sort[i],new_list_sort[i + 1])
                if value:
                    swap(new_list_sort, i, i+1)
                    again = True
        return new_list_sort

def string_length_compare(a, b):
    return len(a) > len(b)

list1 = [ 'abcde', 'xy', 'm', 'rqc', 'jwif' ]

print(" Variable list1 to be sorted: ", list1)
sorted_list1 = simple_sort( list1, string_length_compare )
print("Variable list1 after the sort:", list1)
print(" Sorted list sorted_list1:", sorted_list1)

print("\nThat's all folks!")