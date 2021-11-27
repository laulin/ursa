Introduction
============

RSA implementation based on `Sybren A. Stüvel's python-rsa <https://github.com/sybrenstuvel/python-rsa>`_ pure-python
RSA implementation.

Modified by Adafruit Industries (https://github.com/adafruit/Adafruit_CircuitPython_RSA) for CircuitPython, the forked version of Micropython

Finally, modified for Micropython.

Dependencies
=============

Standalone version.

Installing
==========

Copy the directory *ursa/* in /pyboard. It can be also be copied to another directory if it is in the PYTHONPATH.

Usage Example
=============

Examples for this library are avaliable in the examples/ folder.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://circuitpython.readthedocs.io/projects/rsa/en/latest/>`_.

Security 
========

Because of how Python internally stores numbers, it is very hard (if not impossible) to make a pure-Python program secure against timing attacks. This library is no exception, so use it with care. See https://securitypitfalls.wordpress.com/2018/08/03/constant-time-compare-in-python/ for more info.
