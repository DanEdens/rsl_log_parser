# proc_a.py

import sys
print "what should proc A say?"
for name in iter(sys.stdin.readline, ''):
    name = name[:-1]
    if name == "exit":
        break
    print "Proc A says, \"{0}\"".format(name)
    print "what should proc A say?"
