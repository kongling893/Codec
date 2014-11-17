#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = {'name' : 'Wei Qiao',
	      'mail' : 'qiaowei@tamu.edu'}


class ArithmeticCoding:
	p_dic = {}   #a dictionary to store the number of occurence of each symbol
	summ = 0.0
	coding_symbols = ""
	coded_symbols = ""

	def __init__(self):
		x=1

	def coder(self,coding_symbols):
		self.coding_symbols = coding_symbols
		self.caculateP(coding_symbols)
		

        def caculateP(self,coding_symbols):
		for s in coding_symbols:
			self.summ = self.summ+1
			if self.p_dic.get(s): self.p_dic[s]=self.p_dic[s]+1.0
			else: self.p_dic[s] = 1.0
		for key in self.p_dic:  
			self.p_dic[key] = self.p_dic[key]/self.summ
		


	def decoder(self,coded_str):
		x=2
		


if __name__=="__main__":
	codec = ArithmeticCoding()
	s=raw_input("Please input the symbols you want to code uisng Huffman:\n")
	codec.coder(s)
	print codec.p_dic
	
		
