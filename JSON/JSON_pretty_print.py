'''
author : Jaydatt Patel

json.dumps(arguments) :

(function) def dumps(
    obj: Any,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: int | str | None = None,
    separators: tuple[str, str] | None = None,
    default: ((Any) -> Any) | None = None,
    sort_keys: bool = False,
    **kwds: Any
) -> str

Serialize obj to a JSON formatted str.

If skipkeys is true then dict keys that are not basic types (str, int, float, bool, None) will be skipped instead of raising a TypeError.

If ensure_ascii is false, then the return value can contain non-ASCII characters if they appear in strings contained in obj. Otherwise, all such characters are escaped in JSON strings.

If check_circular is false, then the circular reference check for container types will be skipped and a circular reference will result in an RecursionError (or worse).

If allow_nan is false, then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (NaN, Infinity, -Infinity).

If indent is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. None is the most compact representation.
The indent parameter specifies the spaces that are used at the beginning of a line. We can use the indent parameter of json.dump() to specify the indentation value. By default, when you write JSON data into a file, Python doesn't use indentations and writes all data on a single line, which is not readable.

If specified, separators should be an (item_separator, key_separator) tuple. The default is (', ', ': ') if *indent* is None and (',', ': ') otherwise. To get the most compact JSON representation, you should specify (',', ':') to eliminate whitespace.

default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.

If *sort_keys* is true (default: False), then the output of dictionaries will be sorted by key.

To use a custom JSONEncoder subclass (e.g. one that overrides the .default() method to serialize additional types), specify it with the cls kwarg; otherwise JSONEncoder is used.

json.dumps() function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. 


'''

import json

var =[
        {
            "word": "money",
            "score": 4415
        },
        {
            "word": "honey",
            "score": 1206
        }   
    ]
print("--------------(1)-------------")
print(json.dumps(var))
print("--------------(2)-------------")
print(json.dumps(var,indent=2))
print("--------------(3)-------------")
print(json.dumps(var,indent=10))
print("--------------(4)-------------")
print(json.dumps(var,indent=2,sort_keys=True))
print("--------------(5)-------------")
print(json.dumps(var,indent=2,sort_keys=True,separators=('; ',' = ')))