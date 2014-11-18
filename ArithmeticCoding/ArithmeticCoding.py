#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = {'name' : 'Wei Qiao',
	      'mail' : 'qiaowei@tamu.edu'}


class ArithmeticCoding:
	p_dic = {}   #a dictionary to store the number of occurence of each symbol
	summ = 0.0
	coding_sequence = ""
	coded_sequence = ""
	coded_symbols = {}
        symbols_table = []
        p_table = []

	def __init__(self):
		x=1

	def coder(self,coding_sequence):
		self.coding_sequence = coding_sequence
		self.caculateP(self.coding_sequence)
	        for (key,val) in self.p_dic.items():#sort keys according to their occurence frequencies
                        self.arrange(key,val)
                self.genCodingtable()
                for s in self.coding_sequence:
                        self.coded_sequence = self.coded_sequence+self.coded_symbols[s]
        def getCodedsequence(self):
                return self.coded_sequence
       
        def genCodingtable(self):
                self.coded_symbols[self.symbols_table[0]] = "0"
                for i in range(1,len(self.symbols_table)):
                       self.coded_symbols[self.symbols_table[i]] = self.coded_symbols[self.symbols_table[i-1]]+"1"
                         
        def arrange(self,key,val):
                for i in range(len(self.p_table)):
                        if(val>self.p_table[i]):
                                self.p_table.insert(i,val)
                                self.symbols_table.instert(i,key)
                                return
                self.p_table.append(val)
                self.symbols_table.append(key)
                


        def caculateP(self,coding_sequence):
		for s in coding_sequence:
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
        for (key,val) in  codec.p_dic.items():
                print key,val
        print codec.getCodedsequence()	
		
