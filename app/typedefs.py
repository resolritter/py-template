from dataclasses import dataclass
from typing import Generic, TypeVar, Union, no_type_check

T = TypeVar("T")


@dataclass
class Ok(Generic[T]):
    v: T


E = TypeVar("E")


@dataclass
class Err(Generic[E]):
    v: E


class Final(type):
    @no_type_check
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, Final):
                raise TypeError(
                    "type '{0}' is not an acceptable base type".format(
                        b.__name__
                    )
                )
        return type.__new__(cls, name, bases, dict(classdict))


class Error:
    pass


class NetworkError(Error):
    __metaclass__ = Final

    def __init__(self, err: str):
        pass


@dataclass
class Point1:
    x: int
    y: int


@dataclass
class Point2:
    x: int
    y: int
