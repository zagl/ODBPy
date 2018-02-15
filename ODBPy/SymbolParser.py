#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ODB++ symbol parser
"""

from collections import namedtuple
from . import StandardSymbols

__all__ = ["parse_symbol_name", "parse_symbol_names"]

_symbol_type_names = (
    "Round",
    "Square",
    "Rectangle",
    "RoundedRectangle",
    "ChamferedRectangle",
    "Oval",
    "Diamond",
    "Octagon",
    "RoundDonut",
    "SquareDonut",
    "SquareRoundDonut",
    "RoundedSquareDonut",
    "RectangleDonut",
    "RoundedRectangleDonut",
    "OvalDonut",
    "HorizontalHexagon",
    "VerticalHexagon",
    "Butterfly",
    "SquareButterfly",
    "Triangle",
    "HalfOval",
    "RoundThermalRounded",
    "RoundThermalSquared",
    "SquareThermal",
    "SquareThermalOpenCorners",
    "SquareRoundThermal",
    "RectangularThermal",
    "RectangularThermalOpenCorners",
    "RoundedSquareThermal",
    "RoundedSquareThermalOpenCorners",
    "RoundedRectangleThermal",
    "RoundedRectangleThermalOpenCorners",
    "OvalThermal",
    "OvalThermalOpenCorners",
    "Ellipse",
    "Moire",
)

_user_symbol = namedtuple("User", ["name", "unit"])

def parse_user_symbol(s):
    s, _, unit = s.partition(" ")
    if unit == "":
        unit = None
    return _user_symbol(s, unit)

def parse_symbol_name(symbol_name):
    for symbol_type_name in _symbol_type_names:
        symbol_type = getattr(StandardSymbols, symbol_type_name)
        symbol = symbol_type.Parse(symbol_name)
        if symbol is not None:
            return symbol
    return parse_user_symbol(symbol_name)

def parse_symbol_names(symbol_names):
    return {
        key: parse_symbol_name(symbol_name)
        for key, symbol_name in symbol_names.items()
    }

