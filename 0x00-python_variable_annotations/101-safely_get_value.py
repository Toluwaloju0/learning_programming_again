#!/usr/bin/python3
""" a module to annotate a callback"""

from typing import TypeVar, Dict, Any, Union

D = TypeVar("d")

def safely_get_value(dct: D, key: Any, default: None = None) -> Union[Any, None]:
    if key in dct:
        return dct[key]
    else:
        return default