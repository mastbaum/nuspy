#!/usr/bin/env python

#
# toolbox.py
#
# definitions of tools (commands) available to run
#
# a Tool's context is where it runs (locally or on network hosts). This affects
# how the host list is interpreted (ping all these hosts vs. run ping on all
# these hosts).
#
# atm (amastbaum@gmail.com), 2011
#

import nuspy

# ping
ping = nuspy.Tool('ping', context = nuspy.local)
ping.command = 'ping -c 1 %(host)s'
ping.return_code_only = True

# qstat
qstat_au = nuspy.Tool('qstat_au', context = nuspy.local)
qstat_au.command = 'qstat %(argument)s | grep %(host)s'
qstat_au.params = {'argument': '-f'}
qstat_au.filter_fcn = lambda s : 'au' in s.split()

# hdparm
hdparm = nuspy.Tool('hdparm', context = nuspy.network)
hdparm.command = 'hdparm -i %(disk)s'

# df
df = nuspy.Tool('df', context = nuspy.network)

connectivity = [ping]
sge = [qstat_au]
disks = []

everything = list(set(connectivity + sge + disks))

