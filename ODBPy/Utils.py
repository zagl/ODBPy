#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gzip
from zipfile import ZipFile
import os
import tarfile
from .unlzw import unlzw

__all__ = ["readFileLines", "readGZIPFileLines", "readZIPFileLines", "try_parse_number",
           "not_none", "const_false"]

def try_parse_number(s):
    """
    Return int(s), float(s) or s if unparsable.
    Also returns s if s starts with 0 unless it is "0" or starts with "0."
    (and therefore can't be treated like a number)
    """
    if s.startswith("0") and len(s) != 1 and not s.startswith("0."):
        return s
    # Try parsing a nmeric
    try:
        return int(s)
    except ValueError: # Try float or return s
        try:
            return float(s)
        except:
            return s

def readFileLines(odbpath, filename, open_fn=open):
    "Get stripped lines of a given file"
    if os.path.isdir(odbpath):
        filepath = os.path.join(odbpath, filename)
        try: # Assume file-like object
            return [l.strip() for l in filepath.read().split("\n")]
        except AttributeError:
            try:
                with open_fn(filepath) as fin:
                    return [l.strip() for l in fin.read().split("\n")]
            except UnicodeDecodeError:
                with open_fn(filepath, encoding='latin-1') as fin:
                    return [l.strip() for l in fin.read().split("\n")]
    elif os.path.isfile(odbpath):
        root, ext = os.path.splitext(odbpath)
        if ext.lower() == ".gz" or ext.lower() == ".tgz":
            with tarfile.open(odbpath) as tar:
                top = os.path.commonprefix(tar.getnames())
                filepath = os.path.join(top, filename).replace(os.path.sep, "/")
                try:
                    binary_content = tar.extractfile(filepath).read()
                except KeyError:
                    stream = tar.extractfile("{}.Z".format(filepath)).read()
                    binary_content = unlzw(stream)

                try:
                    content = binary_content.decode("utf-8")
                except UnicodeDecodeError:
                    content = binary_content.decode("latin-1")

                return [l.strip() for l in content.split("\n")]

        else:
            raise IOError("Wrong file type: {}".format(odbpath))
    else:
        raise IOError("File does not exist: {}".format(odbpath))

def readGZIPFileLines(odbpath, filename):
    "Get stripped lines of a given file in gzip format"
    return readFileLines(odbpath, filename, open_fn=gzip.open)

def readZIPFileLines(odbpath, filename, codec="utf-8"):
    "Get stripped lines of a given ZIP file containing only one entry"
    with ZipFile(os.path.join(odbpath, filename), 'r') as thezip:
        names = thezip.namelist()
        if len(names) != 1:
            raise ValueError("ZIP files does not contain exactly one file: {}".format(names))
        return [l.strip() for l in
                thezip.read(names[0]).decode(codec).split("\n")]

def not_none(x):
    "Return True exactly if x is not None. Mostly used as a filter predicate."
    return x is not None

def const_false():
    "Always return False. Used in place of a lambda."
    return False
