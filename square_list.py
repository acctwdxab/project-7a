# Dan Wu
# 11/12/2020
# Write a function that takes as a parameter a list of numbers and replaces each value with the square of that value.

def square_list(lst):
     """takes a list of numbers and replaces each value with the square of that value"""
     for i in range ( len (lst)):
          lst[i] = lst[i] ** 2


