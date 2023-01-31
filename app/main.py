#!/bin/env python

from typing_extensions import assert_never

from app.typedefs import Err, Ok, Point1, Point2


def fetch_point() -> Ok[Point1 | Point2] | Err[str]:
    from random import randint

    result = randint(1, 3)
    match result:
        case 1:
            return Ok(Point1(0, 0))
        case 2:
            return Ok(Point2(0, 0))
        case _:
            return Err("Unknown error")


def repr(input: Ok[Point1 | Point2] | Err[str]):
    match input:
        case Ok(point):
            match point:
                case Point1(0, y):
                    return f"Y={y}"
                case Point1(x, 0):
                    return f"X={x}"
                case Point1(_, y) if y > 3:
                    return "Too far!"
                case Point1(x, y):
                    return f"X={x}, Y={y}"
                case Point2(x, y):
                    return f"X={x}, Y={y}"
                case _:
                    assert_never(point)
        case Err(error):
            return f"ERROR! {error}"
        case _:
            assert_never(input)


def main():
    print(f"repr={repr(fetch_point())}")


if __name__ == "__main__":
    main()
