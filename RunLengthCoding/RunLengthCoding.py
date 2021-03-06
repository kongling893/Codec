#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

__author__ = {'name' : 'Wei Qiao',
	      'mail' : 'qiaowei@tamu.edu',
	      'scheme': 'Run-Length coding'}

#In this coding scheme, we just give a simple example to show run-length coding.
#Run-length coding is efficiennt for binary source. It has been included into JPEG compression.


class RunLengthCoding:
	def __init__(self):
		self.coding_sequence = ""
		self.coded_sequence = ""
		self.decoded_sequence = ""
	def encoder(self,coding_sequence):
		if(coding_sequence == "" or type(coding_sequence)!=str): return
		self.coding_sequence = coding_sequence
		count = 1
		c = coding_sequence[0]
		for i in range(1,len(self.coding_sequence)):
			s = self.coding_sequence[i]
			if s == c: 
				count=count+1
			else:
				self.coded_sequence = self.coded_sequence+str(count)+c
				count = 1
				c=s

	def decoder(self,coded_sequence):
		if(coded_sequence == "" or type(coded_sequence)!=str): return
		if(len(coded_sequence)%2!=0):
			print "wrong input"
			return
		for i in range(len(coded_sequence)):
			if i%2 == 0:
				N =  coded_sequence[i]
			else:	
				c = coded_sequence[i]
				for j in range(int(N)):
					self.decoded_sequence = self.decoded_sequence+c

	def getCodedSequence(self):
		return self.coded_sequence

	def getDecodedSequence(self):
		return self.decoded_sequence
				


if __name__=="__main__":
	coding_sequence = "11110000111001"
	print "The coding sequence is:"+coding_sequence
	coder = RunLengthCoding()
	coder.encoder(coding_sequence)
	print "The encoded sequence is:"+coder.getCodedSequence()
	coder.decoder(coder.getCodedSequence())
	print "The decoded sequence is:"+coder.getDecodedSequence()
	
	

	



