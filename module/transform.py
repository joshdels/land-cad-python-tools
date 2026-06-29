from traverse import TraversePoint


def transform_to_blm(
    traverse_list: list[TraversePoint],
    origin_easting: float,
    origin_northing: float,
) -> list[TraversePoint]:
    """
    Translate local traverse coordinates to BLM/project coordinates.
    """

    new_array: list[TraversePoint] = []

    for point in traverse_list:
        x = point.x + origin_easting
        y = point.y + origin_northing

        new_array.append(
            TraversePoint(
                point=point.point,
                x=x,
                y=y,
            )
        )

    return new_array
