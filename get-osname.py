#!/usr/bin/env python

import sys
if sys.platform.startswith('win32'):
 print("Windows")
elif sys.platform.startswith('linux2'):
 print("Linux")
elif sys.platform.startswith('cygwin'):
 print("Windows/Cygwin")
elif sys.platform.startswith('darwin'):
 print("Mac OS X")
elif sys.platform.startswith('os2'):
 print("OS/2")
elif sys.platform.startswith('os2emx'):
 print("OS/2 EMX")
elif sys.platform.startswith('riscos'):
 print("RiscOS")
elif sys.platform.startswith('atheos'):
 print("AtheOS")

