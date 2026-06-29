import math
from dataclasses import dataclass


@dataclass
class CoordinateDelta:
    dx: float
    dy: float


def traverse_leg(data) -> CoordinateDelta:
    """
    Convert a single bearing leg into coordinate deltas.

    Args:
        data: BearingLeg(ns, degrees, minutes, ew, distance)

    Returns:
        CoordinateDelta(dx, dy)
    """
    try:
        angle = data.degrees + (data.minutes / 60)
        theta = math.radians(angle)

        dx = data.distance * math.sin(theta)
        dy = data.distance * math.cos(theta)

        if data.ns == "S":
            dy *= -1

        if data.ew == "W":
            dx *= -1

        return CoordinateDelta(dx, dy)

    except AttributeError as e:
        raise ValueError("Invalid Bearing object") from e


@dataclass
class TraversePoint:
    point: int
    x: float
    y: float


def build_traverse(legs) -> list[TraversePoint]:
    """
    Build the traverse from a list of bearing legs.

    Args:
        legs: List of BearingLeg objects.

    Returns:
        List[TraversePoint]
    """

    try:
        x = 0.0
        y = 0.0

        points = [TraversePoint(point=0, x=x, y=y)]

        for i, leg in enumerate(legs, start=1):
            coordinate_delta = traverse_leg(leg)

            x += coordinate_delta.dx
            y += coordinate_delta.dy

            points.append(TraversePoint(point=i, x=x, y=y))

        return points

    except Exception as e:
        raise RuntimeError("Faile to build traverse") from e
