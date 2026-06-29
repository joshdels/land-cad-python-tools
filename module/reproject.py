from pyproj import Transformer
from traverse import TraversePoint


def reproject(traverse, from_crs, to_crs):
    transformer = Transformer.from_crs(from_crs, to_crs, always_xy=True)

    new_points = []

    for p in traverse:
        x, y = transformer.transform(p.x, p.y)

        new_points.append(
            TraversePoint(
                point=p.point,
                x=x,
                y=y,
            )
        )

    return new_points
