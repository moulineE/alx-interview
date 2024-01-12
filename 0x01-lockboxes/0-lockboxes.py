#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened
    Args:
        boxes: a list of lists("the boxes")
    Returns:
        True  if all boxes can be opened
        False otherwise
    """
    if type(boxes) is not list or any(type(box) is not list for
                                      box in boxes) or len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for nkey in boxes[key]:
            if nkey not in keys and nkey <= (len(boxes) - 1):
                keys.append(nkey)
    if len(keys) == len(boxes):
        return True
    return False
