#!/usr/bin/python3
"""
lockboxes solution module
"""


def canUnlockAll(boxes):
    """
    CanunlockAll: Determines if a list of lock boxes can be opened
    based on keys that can be attained.
    Returns:
        True if the boxes can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
