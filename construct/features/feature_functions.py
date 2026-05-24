"""
DATE: 24.05.2026
NAME: MARTIN
PURPOSE:
In this file all functions that lie in the folder "construct/features" are stored as wrappers.
If constructing something, by using a function: Always refer to the functions in this file and never to the functions directly.
"""

from construct.features.NAME.infer_name import _infer_name

def infer_name(x1, x2):
    return _infer_name(x1, x2)