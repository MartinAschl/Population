"""
DATE: 24.05.2026
NAME: MARTIN
PURPOSE:
In this file all functions that lie in the folder "construct/features" are stored as wrappers.
If constructing something, by using a function: Always refer to the functions in this file and never to the functions directly.
"""

def infer_gender():
    from construct.features.GENDER.infer_gender import _infer_gender
    return _infer_gender()

def infer_date_of_birth():
    from construct.features.DATE_OF_BIRTH.infer_date_of_birth import _infer_date_of_birth
    return _infer_date_of_birth()

def infer_name(x1, x2):
    from construct.features.NAME.infer_name import _infer_name
    return _infer_name(x1, x2)



