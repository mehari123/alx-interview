
#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""


def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """
    
    keys=[]
    for index,box in enumerate(boxes):
        for key in box:
            if key!=index:
                keys.append(key)
   
    size1=len(boxes)
    for num in range(1,size1):
        if num not in keys:
            return False
    return True
    
