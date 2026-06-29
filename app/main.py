from module import parse_bearing
from module.traverse import build_traverse
from module.transform import transform_to_blm
from module.reproject import reproject
from module.exporter.geojson import convert_geojson

bearing_texts = [
    "S 11. 48 W 1351",
    "S 4. 47 E 79.70m",
    "S 89 deg. 37   W 67.41",
    "S 87deg. 18 W 65.41m",
    "N 3deg.  07W 27.93m",
    "N 18 25 W 38.15",
    "N 82 17 E 140.55",
]

bearings = []

for text in bearing_texts:
    bearing = parse_bearing(text)
    bearings.append(bearing)


# Conversion
traverse_points = build_traverse(bearings)
print(traverse_points)

traverse = transform_to_blm(traverse_points, 446673.805, 1767616.817)
print(traverse)

reproject = reproject(traverse, "EPSG:3123", "EPSG:4326")

result = convert_geojson(reproject)
print(result)
