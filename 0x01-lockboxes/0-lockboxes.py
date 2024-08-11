#!/usr/bin/python3
"""
Lockboxes Algorithm
"""


def canUnlockAll(boxes):
    """
    Function determines if all boxes in a given list can be ultimately opened.
    Args:
        boxes(list of lists): Boxes
    Return:
        (bool): True if all boxes can be opened, otherwise, False
    """
    if not isinstance(boxes, list):
        return False
    if not all(isinstance(box, list) for box in boxes):
        return False

    # DEPTH-FIRST SEARCH
    visited = set()
    to_visit = [0]  # Stack: visit first box first since its unlocked
    n = len(boxes)

    while to_visit:
        current_index = to_visit.pop()

        # Only visit unvisited boxes and boxes at valid index
        if current_index in visited or current_index >= n:
            continue

        visited.add(current_index)
        to_visit.extend(boxes[current_index])  # Add keys in this box to stack

    return len(visited) == len(boxes)

#    BREADTH-FIRST SEARCH
#    from collections import deque
#
#    visited = set()
#    to_visit = deque([0])  # Queue: visit first box first since its unlocked
#
#    while to_visit:
#        current_index = to_visit.popleft()
#        if current_index in visited:
#            continue
#        visited.add(current_index)
#        to_visit.extend(boxes[current_index])  # add keys here to queue
#
#        """For visual display"""
#        print(f"Just visited box[{current_index}]")
#        print(f"Total visited {visited}")
#        print(f"To visit: {to_visit}")
#        print()
#
#    return len(visited) == len(boxes)
