#!/usr/bin/env python
import os 
import sys
import visa
import time
#-------------------------------------------------------------#
## main function 
# @param there is no parameter for main function
def main():
	rm = visa.ResourceManager()
	print rm.list_resources()
	#instr = rm.open_resource('USB0::0x1AB1::0x0641::DG4E172601737::INSTR')
	#print instr.query("*IDN?")
	#instr.write(":VOLTage 5")
	# time.sleep(0.5)
	# instr.write(":VOLTage:OFFSet 1")
	# time.sleep(0.5)
	# print instr.query(":VOLTage:OFFSet?")
	# time.sleep(5)
	# for i in xrange(100):
	# 	instr.write(":SOURce2:FREQuency %s"%((i+1)*100))
	# 	time.sleep(0.5)
	# 	print instr.query(":SOURce2:FREQuency?")			#query instruction equals write then read
	# 	time.sleep(1.0)
	# 	instr.write(":SOURce1:FREQuency %s"%((i+1)*100))
	# 	time.sleep(0.5)
	# 	print instr.query(":SOURce1:FREQuency?")			#query instruction equals write then read
	# 	time.sleep(1.0)
#-------------------------------------------------------------#
## if statement
if __name__ == '__main__':
	sys.exit(main()) 