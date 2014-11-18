#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

__author__ = {'name' : 'Wei Qiao',
	      'mail' : 'qiaowei@tamu.edu',
	      'scheme': 'LZW coding'}


class LZWCoding:
	def __init__(self):
		self.coded_sequence = ""
		self.init_codeTable = {}
		self.init_decodeTable = {}
		self.coded_sequence = []
		self.decoded_sequence = ""
	def initCodeingTable(self):
		i = 0
		for s in self.coding_sequence:
			if self.init_codeTable.get(s)==None: 
				self.init_codeTable[s] = i
				i=i+1
	
	def encoder(self,coding_sequence):
		self.coding_sequence = coding_sequence
		self.initCodeingTable()
		self.coding_table = copy.deepcopy(self.init_codeTable)
		N = len(self.coding_table)
		if self.coding_sequence == "": return
		s = self.coding_sequence[0]
	        for i in range(1,len(self.coding_sequence)):
			c = self.coding_sequence[i]
			if self.coding_table.get(s+c)==None:
				self.coded_sequence.append(self.coding_table[s])
				self.coding_table[s+c] = N
				s = c
				N=N+1
			else:
				s=s+c
		if self.coding_table.get(s)==None:
			self.coding_table[s+c] = N
		self.coded_sequence.append(self.coding_table[s])                
      
        def getCodedsequence(self):
                return self.coded_sequence
       
       	def initDecodeingTable(self): 
		#note here, for both initial coding and decoding tables, since we know all the sigle characters before we encode and decode,
		#it's easy to generate the initial tables.
		for (key,val) in self.init_codeTable.items():
			self.init_decodeTable[val] = key

	def decoder(self): 
		self.initDecodeingTable()
		self.decoding_table = copy.deepcopy(self.init_decodeTable)
	        s = self.coded_sequence[0]
		self.decoded_sequence = self.decoded_sequence+self.decoding_table[s]
		j=len(self.decoding_table)
                for i in range(1,len(self.coded_sequence)): 
			p = s
			s = self.coded_sequence[i]
			if self.decoding_table.get(s)!=None:
				self.decoded_sequence = self.decoded_sequence+self.decoding_table[s]
				k = self.decoding_table[s]
				self.decoding_table[j] = self.decoding_table[p]+k
				j = j+1
			else:
				self.decoded_sequence = self.decoded_sequence+self.decoding_table[s]
				k = self.decoding_table[p]
				self.decoding_table[j] = self.decoding_table[p]+k
				j = j+1
				

	def getDecodedsequence(self):
                return self.decoded_sequence
			
		


if __name__=="__main__":
	codec = LZWCoding()
	s=raw_input("Please input the symbols you want to code uisng LZW coding:\n")
	codec.encoder(s) 
	print "the coded sequence is:" 
        print codec.getCodedsequence()	
	print "the coding table is:"
	print codec.coding_table
	codec.decoder()
	print "the decoded sequence is:"	
	print codec.getDecodedsequence()
	print "the decoding table is:"	
	print codec.decoding_table
		
