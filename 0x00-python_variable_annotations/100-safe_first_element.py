#!/usr/bin/env python3
""" a module to annotate types that are not known """

from typing import List, Any, Union

def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
