
import re

text = 'N 14 deg. 15\' E'

pattern_direction= r"[NSEW]"
pattern_digits = r"\d{2}"

direction = re.findall(pattern_direction, text)
digits = re.findall(pattern_digits, text)


print(direction)
print(digits)