import re
from dataclasses import dataclass


@dataclass
class BearingLeg:
    ns: str
    degrees: int
    minutes: int
    ew: str
    distance: float


def parse_bearing(text: str) -> BearingLeg:
    """
    Parse a bearing string.
    NS | Degree | Minutes | EW | Distance(m)

    Examples:
        N 14 deg. 15' E 100m,
        S 45 deg 30 W 200m,


    """

    try:
        directions = re.findall(r"[NSEW]", text)
        numbers = re.findall(r"\d+\.?\d*", text)
        distance = float(numbers[-1])

        return BearingLeg(
            ns=directions[0],
            degrees=numbers[0],
            minutes=numbers[1],
            ew=directions[1],
            distance=distance,
        )

    except ValueError:
        raise

    except Exception as e:
        raise RuntimeError(f"Failed to parse bearing: '{text}'") from e
