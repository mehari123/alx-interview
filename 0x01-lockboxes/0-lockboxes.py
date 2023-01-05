#!/usr/bin/python3
def canUnlockAll(boxes):
    
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
    