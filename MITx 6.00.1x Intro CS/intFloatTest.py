#Python test on if it is a int or float.

>>> h = "1.1"

>>> int(h) if "." not in h else float(h)
1.1

>>> h = "1"

>>> int(h) if "." not in h else float(h)
1

>>> float(h) if float(h) % 1 else int(h)
1

>>> h = "1.1"

>>> float(h) if float(h) % 1 else int(h)
1.1
