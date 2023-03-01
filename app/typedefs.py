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


@dataclass
class Point1:
    x: int
    y: int


@dataclass
class Point2:
    x: int
    y: int
