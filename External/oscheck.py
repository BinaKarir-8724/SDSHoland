#!usr/bin/env python

import platform

platform = platform.system()
if platform == "Linux" :
	print("Aplikasi ini dijalankan dalam sistem operasi Linux")
	paths = "/Apps"
elif platform == "Windows" :
	print ("Aplikasi ini dijalankan dalam sistem operasi Windows")
	paths = "\Apps"
else :
	print ("Sistem Operasi Lainnya")
	pass
