import json

def convert_geojson(traverse, filename="parcel.geojson"):

    feature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [[p.x, p.y] for p in traverse],
        },
    }

    geojson = {
        "type": "FeatureCollection",
        "features": [feature],
    }

    with open("parcel.geojson", "w") as f:
        json.dump(geojson, f, indent=2)
