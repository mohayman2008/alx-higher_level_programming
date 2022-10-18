#!/usr/bin/python3
def magic_string():
    __annotations__["s"] = __annotations__.get("s", "") + "BestSchool, "
    return (__annotations__["s"][:-2])
