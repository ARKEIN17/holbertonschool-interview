#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    unlocked = [0]
    for index, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != index:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False