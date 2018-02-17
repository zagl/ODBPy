#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ODB++ standard symbol geometries
See ODB++ 7.0 spec page 202++
"""
import re
from enum import Enum
from collections import namedtuple
import functools
from .Structures import HolePlating


def _parse_allfloat(rgx, constr, s):
    """
    Parse a string using a regex yielding only floats group
    """
    s, _, unit = s.partition(" ")
    match = rgx.match(s)
    if match is None:
        return None
    args = list(map(float, match.groups()))
    if unit is not "":
        args.append(unit)
    return constr(*args)


def _parse_allfloat_corners(rgx, constr, s):
    """
    Parse a string using a regex yielding only floats group,
    with the exception of the last group, being an optional corner
    group containing a list of corners
    """
    s, _, unit = s.partition(" ")
    match = rgx.match(s)
    if match is None:
        return None
    groups = match.groups()
    # Treat last group separately
    cornersStr = groups[-1] if groups[-1] is not None else "1234"
    corners = [int(c) for c in cornersStr if c.isdigit()]
    # Assemble args list
    args = list(map(float, groups[:-1]))
    args.append(corners)
    if unit is not "":
        args.append(unit)
    return constr(*args)


def _standard_symbol_factory(name, regex, field_names, parsefunc):
    """
    Generates a new standard symbol container class
    (derived from namedtuple) from a matcher regex,
    a list of fields and one of the _parse_... parsers
    from this module
    """
    _cls = namedtuple(name, field_names + ["unit"])
    _cls.__new__.__defaults__ = (None,) * len(_cls._fields)
    _cls.regex = re.compile(regex)
    _cls.Parse = functools.partial(parsefunc, _cls.regex, _cls)
    return _cls


Round = _standard_symbol_factory("Round", r"^r([\.\d]+)$", ["diameter"], _parse_allfloat)

Square = _standard_symbol_factory("Square", r"^s([\.\d]+)$", ["side"], _parse_allfloat)

Rectangle = _standard_symbol_factory("Rectangle", r"^rect([\.\d]+)x([\.\d]+)$",
    ["width", "height"], _parse_allfloat)

RoundedRectangle = _standard_symbol_factory("RoundedRectangle",
    r"^rect([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["width", "height", "corner_radius", "corners"], _parse_allfloat_corners)

ChamferedRectangle = _standard_symbol_factory("ChamferedRectangle",
    r"^rect([\.\d]+)x([\.\d]+)xc([\.\d]+)(x[\.\d]+)?$",
    ["width", "height", "corner_radius", "corners"], _parse_allfloat_corners)

Oval = _standard_symbol_factory("Oval", r"^oval([\.\d]+)x([\.\d]+)$", ["width", "height"], _parse_allfloat)

Diamond = _standard_symbol_factory("Diamond",
    r"^di([\.\d]+)x([\.\d]+)$", ["width", "height"], _parse_allfloat)

Octagon = _standard_symbol_factory("Octagon",
    r"^oct([\.\d]+)x([\.\d]+)x([\.\d]+)$", ["width", "height", "corner_size"], _parse_allfloat)

RoundDonut = _standard_symbol_factory("RoundDonut",
    r"^donut_r([\.\d]+)x([\.\d]+)$", ["outer_diameter", "inner_diameter"], _parse_allfloat)

SquareDonut = _standard_symbol_factory("SquareDonut",
    r"^donut_s([\.\d]+)x([\.\d]+)$", ["outer_diameter", "inner_diameter"], _parse_allfloat)

SquareRoundDonut = _standard_symbol_factory("SquareRoundDonut",
    r"^donut_sr([\.\d]+)x([\.\d]+)$", ["outer_diameter", "inner_diameter"], _parse_allfloat)

RoundedSquareDonut = _standard_symbol_factory("RoundedSquareDonut",
    r"^donut_s([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_diameter", "inner_diameter", "corner_radius", "corners"], _parse_allfloat_corners)

RectangleDonut = _standard_symbol_factory("RectangleDonut",
    r"^donut_rc([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_diameter", "inner_diameter", "line_width"], _parse_allfloat)

RoundedRectangleDonut = _standard_symbol_factory("RoundedRectangleDonut",
    r"^donut_rc([\.\d]+)x([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_diameter", "inner_diameter", "line_width", "corner_radius", "corners"], _parse_allfloat_corners)

OvalDonut = _standard_symbol_factory("OvalDonut",
    r"^donut_o([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_diameter", "inner_diameter", "line_width"], _parse_allfloat)

HorizontalHexagon = _standard_symbol_factory("HorizontalHexagon",
    r"^hex_l([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["width", "height", "corner_size"], _parse_allfloat)

VerticalHexagon = _standard_symbol_factory("VerticalHexagon",
    r"^hex_s([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["width", "height", "corner_size"], _parse_allfloat)

Butterfly = _standard_symbol_factory("Butterfly",
    r"^bfr([\.\d]+)$", ["diameter"], _parse_allfloat)

SquareButterfly = _standard_symbol_factory("SquareButterfly",
    r"^bfs([\.\d]+)$", ["size"], _parse_allfloat)

Triangle = _standard_symbol_factory("Triangle",
    r"^tri([\.\d]+)x([\.\d]+)$", ["base", "height"], _parse_allfloat)

HalfOval = _standard_symbol_factory("HalfOval",
    r"^oval_h([\.\d]+)x([\.\d]+)$", ["width", "height"], _parse_allfloat)

RoundThermalRounded = _standard_symbol_factory("RoundThermalRounded",
    r"^thr([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_diameter", "inner_diameter", "angle", "num_spokes", "gap"], _parse_allfloat)

RoundThermalSquared = _standard_symbol_factory("RoundThermalSquared",
    r"^ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_diameter", "inner_diameter", "angle", "num_spokes", "gap"], _parse_allfloat)

SquareThermal = _standard_symbol_factory("SquareThermal",
    r"^s_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_size", "inner_size", "angle", "num_spokes", "gap"], _parse_allfloat)

SquareThermalOpenCorners = _standard_symbol_factory("SquareThermalOpenCorners",
    r"^s_tho([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_diameter", "inner_diameter", "angle", "num_spokes", "gap"], _parse_allfloat)

SquareRoundThermal = _standard_symbol_factory("SquareRoundThermal",
    r"^sr_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_size", "inner_diameter", "angle", "num_spokes", "gap"], _parse_allfloat)

RectangularThermal = _standard_symbol_factory("RectangularThermal",
    r"^rc_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_width", "outer_height", "angle", "num_spokes", "gap", "air_gap"], _parse_allfloat)

RectangularThermalOpenCorners = _standard_symbol_factory("RectangularThermalOpenCorners",
    r"^rc_tho([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_width", "outer_height", "angle", "num_spokes", "gap", "air_gap"], _parse_allfloat)

RoundedSquareThermal = _standard_symbol_factory("RoundedSquareThermal",
    r"^s_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_size", "inner_size", "angle", "num_spokes", "gap", "corner_radius", "corners"],
    _parse_allfloat_corners)

RoundedSquareThermalOpenCorners = _standard_symbol_factory("RoundedSquareThermalOpenCorners",
    r"^s_tho([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_size", "inner_size", "angle", "num_spokes", "gap", "corner_radius", "corners"],
    _parse_allfloat_corners)

RoundedRectangleThermal = _standard_symbol_factory("RoundedRectangleThermal",
    r"^rc_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_width", "outer_height", "line_width", "angle", "num_spokes", "gap", "corner_radius", "corners"],
    _parse_allfloat_corners)

RoundedRectangleThermalOpenCorners = _standard_symbol_factory("RoundedRectangleThermalOpenCorners",
    r"^rc_tho([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)xr([\.\d]+)(x[\.\d]+)?$",
    ["outer_width", "outer_height", "line_width", "angle", "num_spokes", "gap", "corner_radius", "corners"],
    _parse_allfloat_corners)

OvalThermal = _standard_symbol_factory("OvalThermal",
    r"^o_ths([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_width", "outer_height", "angle", "num_spokes", "gap", "line_width"], _parse_allfloat)

OvalThermalOpenCorners = _standard_symbol_factory("OvalThermalOpenCorners",
    r"^o_tho([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["outer_width", "outer_height", "angle", "num_spokes", "gap", "line_width"], _parse_allfloat)

Ellipse = _standard_symbol_factory("Ellipse",
    r"^el([\.\d]+)x([\.\d]+)$", ["width", "height"], _parse_allfloat)

Moire = _standard_symbol_factory("Moire",
    r"^moire([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)x([\.\d]+)$",
    ["ring_width", "ring_gap", "num_rings", "line_width", "line_length", "line_angle"], _parse_allfloat)


_plating_map = {
    "p": HolePlating.Plated,
    "n": HolePlating.NonPlated,
    "v": HolePlating.Via,
}

class Hole(namedtuple("Hole", ["diameter", "plating", "tolerance_plus", "tolerance_minus"])):
    regex = re.compile(r"^hole([\.\d]+)x([pnv])x([\.\d]+)x([\.\d]+)$")

    @staticmethod
    def Parse(s):
        match = Hole.regex.match(s)
        if match is None:
            return None
        a, platingStr, b, c = match.groups()
        return Hole(float(a), _plating_map[platingStr], float(b), float(c))
