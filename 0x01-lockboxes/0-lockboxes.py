""" a module to define the lockboxes function """

def canUnlockAll(boxes):
    """ a function to check if a group of boxed can be opened 
    Args:
        boxes (list of list): the box to be opened 
    """

    keys = {0}

    while True:
        key_len = len(keys)
        for a in range(len(boxes)):
            if a not in keys:
                continue
            for b in boxes[a]:
                keys.add(b)
        if key_len == len(boxes):
            return True
        elif key_len == len(keys):
            return False
