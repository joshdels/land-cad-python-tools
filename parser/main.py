from parser import parse_bearing
from traverse import build_traverse
from transform import transform_to_blm

bearing_texts = [
    "N 10deg. 15 E 200.00",
    "S 45deg. 30 W 210.0m",
    "N 80deg. 45 E 390.1m",
    "S 15deg. 35 E 205m",
]

bearings = []

for text in bearing_texts:
    bearing = parse_bearing(text)
    bearings.append(bearing)



# Conversion
traverse_points = build_traverse(bearings)
print(traverse_points)

traverse = transform_to_blm(traverse_points, 500000.000, 1500000.000)
print(traverse)
