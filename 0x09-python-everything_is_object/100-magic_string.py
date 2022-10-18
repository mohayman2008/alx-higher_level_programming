#!/usr/bin/python3
def magic_string(ds={}):
    ds["s"] = ds.get("s", "") + "BestSchool, "
    return (ds["s"][:-2])
