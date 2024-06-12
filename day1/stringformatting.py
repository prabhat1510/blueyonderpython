# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:34:05 2024

@author: UD SYSTEMS
"""

# string formatting demo

str1="Good"#0123
str2="Morning"


st='{} {}'.format(str1, str2)
print("format function : ",st)

st='{1} {0}'.format(str1, str2)
print("changing position : ",st)

st='{:.3}'.format(str1)
print("String truncate : ",st)
print(str1+str2)

st='{}{}'.format(str1, str2)
print("format function : ",st)

# String filled with hash on right side and its left alinged
st='{:#<10}'.format(str1)
print("Left Aligned Text : ",st)

# String is Right Aligned with minimum width 10
st='{:0>10}'.format(str1)
print("Right Aligned Text : ",st)

# String is center Aligned with minimum width 10
st='{:#^10}'.format('Goods')
print("Center Aligned Text : ",st)
