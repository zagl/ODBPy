#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ODB++ unit utilities
"""
import re

__all__ = ["linerecords_unit", "to_mm", "to_mil", "to_micrometers", "to_inch"]

_unit_line_re = re.compile(r"UNITS=([A-Z]+)")
_unit_line_v7_re = re.compile(r"U\s+([A-Z]+)")

def linerecords_unit(linerecords):
    """
    Given a linerecord dictionary, extract the unit string
    """
    if "Header" in linerecords: # post V8.0
        header_lines = linerecords["Header"]
        # Try to match regex
        match = _unit_line_re.match(header_lines[0])
        if match is None:
            raise ValueError("Invalid unit line: {}".format(unit_lines[0]))
        return match.group(1)

    elif "Units" in linerecords: # pre v8.0
        unit_lines = linerecords["Units"]
        if len(unit_lines) != 1:
            raise ValueError("More than one unit line: {}".format(unit_lines))
        # Try to match regex
        match = _unit_line_v7_re.match(unit_lines[0])
        if match is None:
            raise ValueError("Invalid unit line: {}".format(unit_lines[0]))
        return match.group(1)

_mm_factors = {
    "MM": 1.0,
    "UM": 0.001,
    "IN": 25.4,
    "INCH": 25.4,
    "MIL": 0.0254
}

def to_mm(value, from_unit):
    """Convert a value in unit <from_unit> to mm"""
    return value * _mm_factors[from_unit.upper()]

def to_mil(value, from_unit):
    """Convert a value in unit <from_unit> to mil"""
    return to_mm(value, from_unit) / _mm_factors["MIL"]

def to_micrometers(value, from_unit):
    """Convert a value in unit <from_unit> to mirometers"""
    return to_mm(value, from_unit) / _mm_factors["UM"]

def to_inch(value, from_unit):
    """Convert a value in unit <from_unit> to inches"""
    return to_mm(value, from_unit) / _mm_factors["IN"]
