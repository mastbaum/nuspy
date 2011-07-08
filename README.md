nuspy
=====

nuspy aims to be a lightweight, flexible, and pythonic tool for keeping tabs on hosts on a network. Hosts to be watched and Tools to watch them with are defined in Python in hosts.py and tools.py, respectively.

nuspy should work either interactively in the Python interpreter, like:

>>> import nuspy
>>> import toolbox
>>> nuspy.mod_print(toolbox)

or, better, as user-written scripts that perform common network monitoring tasks

