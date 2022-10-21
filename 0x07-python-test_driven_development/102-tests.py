#!/usr/bin/python3
"""
>>> import ctypes

>>> lib = ctypes.CDLL('./libPython.so')
>>> lib.print_python_string.argtypes = [ctypes.py_object]

>>> s = "The spoon does not exist"
>>> lib.print_python_string(s)
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist

>>> s = "ложка не существует"
>>> lib.print_python_string(s)
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует

>>> s = "La cuillère n'existe pas"
>>> lib.print_python_string(s)
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas

>>> s = "勺子不存在"
>>> lib.print_python_string(s)
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在

>>> s = "숟가락은 존재하지 않는다."
>>> lib.print_python_string(s)
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.

>>> s = "スプーンは存在しない"
>>> lib.print_python_string(s)
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない

>>> s = b"The spoon does not exist"
>>> lib.print_python_string(s)
[.] string object info
  [ERROR] Invalid String Object

"""
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
