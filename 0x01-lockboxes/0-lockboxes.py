#!/usr/bin/python3
"""Module that containes canUnlockAll method"""


def canUnlockAll(boxes):
    if len(boxes) == 0 or isinstance(boxes, list) is False:
        return False

    opened_boxes = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)
