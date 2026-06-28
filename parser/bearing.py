import re

# problem 1
# Line A: "N 14 deg. 15' E"
# Line B: "N14deg.15'E"

#problem 2
# surverying
# "Thence N 45 deg. 20' E a distance of 150.32 feet to a pipe"

# Proble 3
# Parsing Northing and Easting Coordinates
# Text: "Pt102,E:643210.55,N:1042302.11,Elev:45.2"

# Problem 4: Full DMS Extraction with Seconds
# Text: "Course: S 89° 12' 05\" W"

# Problem 5: Identifying the Quadrant First
# Text: "Bearing: N 54 deg. 32' W"

# line = "N 14 deg. 15' E"
# degree = ""
# second = ""
# direction = ""

# match = re.search(r'/d')
# print(match)

import re

pattern = r"\S+\d"

# text = """
# Hello John,

# Please email me at john@gmail.com.

# For support contact support@company.com 12123

# Thanks!

# # Line A: "N 14 deg. 15' E"
# """

import re

text = 'N 14 deg. 15\' E'

pattern_direction= r"[NSEW]"
pattern_digits = r"\S+\d"

direction = re.findall(pattern_direction, text)
digits = re.findall(pattern_digits, text)


print(direction)
print(digits)