#!/usr/bin/env python

#
# hosts.py
#
# "host groups" are just a list of Hosts, which can be added, etc., like any
# python list.
#
# atm (amastbaum@gmail.com), 2011
#

import nuspy

localhost = nuspy.Host('localhost')
me = [localhost]

nubar2 = nuspy.Host('nubar2')
nubar3 = nuspy.Host('nubar3')
nubar4 = nuspy.Host('nubar4')
nubar5 = nuspy.Host('nubar5')
nubar6 = nuspy.Host('nubar6')
nubar7 = nuspy.Host('nubar7')
nubar8 = nuspy.Host('nubar8')
nubar9 = nuspy.Host('nubar9')
nodes = [nubar2, nubar3, nubar4, nubar5, nubar6, nubar7, nubar8, nubar8, nubar9]

macho = nuspy.Host('macho')
wimp = nuspy.Host('wimp')
bigdisk = nuspy.Host('bigdisk')
disk_servers = [macho, wimp, bigdisk]

everything = me + nodes + disk_servers

