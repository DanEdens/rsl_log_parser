# proc_b.py

import sys
print "what should proc B say?"
for name in iter(sys.stdin.readline, ''):
    name = name[:-1]
    if name == "exit":
        break
    print "Proc B says, \"{0}\"".format(name)
    print "what should proc B say?"
