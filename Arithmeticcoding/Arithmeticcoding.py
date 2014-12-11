#/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = {'name' : 'Wei Qiao',
	      'mail' : 'qiaowei@tamu.edu',
	      'scheme': 'Arithmetic Coding',
		}


class Arithmeticcoding:
	def __init__(self):
		self.p_dic = {}   #a dictionary to store the number of occurences of each symbol
		self.summ = 0.0
		self.coding_sequence = ""
		self.coded_sequence = ""
        	self.decoded_sequence = ""
		self.coding_dic = {}
        	self.decoding_dic = {}
        	self.symbols_table = []
		self.p_table = []
                self.cp_table = []


	def encoder(self,coding_sequence):
                lower = 0
                upper = 1
		self.coding_sequence = coding_sequence
		self.calculateP(self.coding_sequence)
	        for (key,val) in self.p_dic.items():#sort keys according to their occurence frequencies
                        self.arrange(key,val)
                self.calculateCP()
                print self.coding_sequence
                for c in self.coding_sequence:
                        for i in range(len(self.symbols_table)):
                                if self.symbols_table[i] == c:
                                        print c
                                        lower1 = lower + (upper-lower)*self.cp_table[i]
                                        upper1 = upper - (upper-lower)*self.cp_table[i+1]
                                        lower = lower1
                                        upper = upper1
                                        print lower,upper
                                        break
                self.coded_number = (upper+lower)/2
                return self.coded_number

        def getCodedsequence(self):
                return self.coded_sequence
               

	def decoder(self):
		#todo
		x=1


        def getDecodedsequence(self):
		return self.decoded_sequence
	
	def calculateP(self,coding_sequence):
		for s in coding_sequence:
			self.summ = self.summ+1
			if self.p_dic.get(s): self.p_dic[s]=self.p_dic[s]+1.0
			else: self.p_dic[s] = 1.0
		for key in self.p_dic:  
			self.p_dic[key] = self.p_dic[key]/self.summ
        
        def calculateCP(self):
                cp = 0
                self.cp_table.append(cp)
                for i in range(len(self.p_table)):
                        cp = cp + self.p_table[i]
                        self.cp_table.append(cp)

	def arrange(self,key,val): #sort the symbols according to their occurrence frequencies  
                for i in range(len(self.p_table)):
                        if(val>self.p_table[i]):
                                self.p_table.insert(i,val)
                                self.symbols_table.insert(i,key)
                                return
                self.p_table.append(val)
                self.symbols_table.append(key)


if __name__=="__main__":
	codec = Arithmeticcoding()
	s=raw_input("Please input the symbols you want to code uisng Arithmetic Coding:\n")
	codec.encoder(s)  
