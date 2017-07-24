#!/usr/bin/env python

import os
import sys
import visa
import time
import numpy as np
import pylab as pl
#-------------------------------------------------------------#
## main function 
# @param there is no parameter for main function
def main():
	rm = visa.ResourceManager()
	print (rm.list_resources())
	instr = rm.open_resource('USB0::0x0699::0x0408::C029817::INSTR')
	print (instr.query("*IDN?"))
	instr.write(":DATa:SOUrce CH1")
	instr.write(":DATa:STARt 1")
	instr.write(":DATa:STOP 10000")
	instr.write(":DATa:ENCdg ASCIi")
	instr.write(":DATa:WIDth 1")
	instr.write(":HEADer 1")
	instr.write(":VERBose")
	instr.write(":HEADer 0")
	print(instr.query(":WFMOutpre?"))
	while(1):
		wav = instr.query(":CURVe?")
		print(list(int(i) for i in wav.split(',')))
	#dict([x.split('=', 1) for x in s.split('&')])

		x1 = range(10000)  # Make x, y arrays for each graph
		y1 = list(int(i) for i in wav.split(','))
		#x2 = [1, 2, 4, 6, 8]
		#y2 = [2, 4, 8, 12, 16]
		pl.plot(x1, y1)  # use pylab to plot x and y
		#pl.plot(x2, y2)
		pl.title('Plot of y vs. x')  # give plot a title
		pl.xlabel('x axis')  # make axis labels
		pl.ylabel('y axis')
		pl.xlim(0.0, 10000.0)  # set axis limits
		pl.ylim(0.0, 100.)
		pl.show()  # show the plot on the screen
		#help(pl)
		time.sleep(1)
		pl.cl
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