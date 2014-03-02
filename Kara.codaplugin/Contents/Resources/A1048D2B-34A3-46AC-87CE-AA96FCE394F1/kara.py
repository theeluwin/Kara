#!/usr/bin/python
import sys
import re
for line in sys.stdin:
	if line[-1] != '\n':
		line += '\n'
	line = re.sub(r'(\t)+\n', '\n', line)
	line = re.sub(r'(\ )+\n', '\n', line)
	sys.stdout.write(line)
sys.stdout.flush()
