#!/usr/bin/env python3
""" a module to annotate a function """

from typing import List, Sequence, Tuple

def element_length(lst: List[Sequence]) -> Tuple[Sequence, int]:
    return [(i, len(i)) for i in lst]