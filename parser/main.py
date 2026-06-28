from parser import parse_bearing

bearing_texts = [
    "N 10deg. 15 E 200m",
    "S 45deg. 30 W 210.0m",
    "N 80deg. 45 E 390.1m",
    "S 15deg. 35 E 205m",
]

bearings = []

for text in bearing_texts:
    bearing = parse_bearing(text)
    bearings.append(bearing)

print(bearings)