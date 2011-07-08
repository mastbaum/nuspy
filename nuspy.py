#!/usr/bin/env python

#
# nuspy.py
#
# a tool for keeping tabs on some computers
#
# atm (amastbaum@gmail.com), 2011
#

import inspect, types

# fixme: do something smarter with this?
local = 'local'
network = 'network'

class Tool:
	'''an external tool we'll use to get a piece of data'''
	def __init__(self, name, context):
		self.name = name
		self.context = context
		command = ''
		return_code_only = False
		filter_fcn = 0
		parameters = {}
	def __repr__(self):
		return self.name

class Host:
	'''a computer'''
	def __init__(self, hostname):
		self.hostname = hostname
	def __repr__(self):
		return self.hostname
	description = ''
	ssh_keyfile = ''

def print_mod(mod):
	for h in inspect.getmembers(mod):
		if h[0][0] != '_' and type(h[1]) is not types.ModuleType:
			if type(h[1]) is types.ListType:
				print h[0], ': (',
				for i in h[1]:
					print i,',',
				print ')'
			else:
				print h[0]

if __name__ == '__main__':
	import sys
	import toolbox
	import hosts

        print '-- Available hosts: -------------------'
	print_mod(hosts)

	print ' -- Available tools: ------------------'
	print_mod(toolbox)

	h = []
	for hostname in sys.argv[1:-1]:
		try:
			h.append(hosts.__dict__[hostname])
		except KeyError:
			print 'nuspy: Host', hostname, 'unknown'

	for e in h:
		try:
	                tool = toolbox.__dict__[sys.argv[-1]]
			args = {'host': e}
			try:
				args.update(tool.params)
			except AttributeError:
				pass
			cmd = tool.command % args
			print cmd
		except KeyError:
			print 'nuspy: Tool', sys.argv[-1], 'not found in toolbox'

