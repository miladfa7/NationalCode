#!/usr/bin/python
import os
from terminaltables import *
import threading
ShowMainHeader=True
ShowHelpHeader=True
ShowValidHeader=True
color={'red':'\033[91m','blue':'\033[94m','black':'\033[90m','green':'\033[92m','end':'\033[1;m','yellow':'\033[93m'}
diccode={"th":"556,658,011,001,002,003,004,005,006,007,020,015,043,048,049,695,659,664,717","zn":"427,428","kh":"163"}
#---------------------------------------- Function Class Codemeli-----------------------------------------------------------------------		
class Codemeli:

	def __init__(self,isSave,FileName=None):
			self.isSave=isSave
			self.FileName=FileName

	def mkCode(self,LC): 

	
		D=LC + "0000000"
		EN=int(LC+"9999999")
		D=int(D)
			
	
		while D<=EN:
			codemeli="%010d" % D #Exact digit number

			if  self.validation(codemeli): #b True bashe in ejra beshe 
				if self.isSave:

					self.__Save(self.FileName,codemeli,"a+")
				else :
					print color.get('blue')+"The Succesfull Scan Code Meli : "+ str(codemeli) + color.get('end')



			D=D+1
	
			


	def validation(self,codemeli):

		b=False
		invali=["0000000000","1111111111","2222222222","3333333333","4444444444","5555555555","6666666666","7777777777","8888888888","9999999999"]

		if codemeli not in invali:
			Sum=0
			for j in range(9):
				Sum+=int(codemeli[j])*(10 - j) #sum number code meli 1-9
			S_C=Sum
			C=(S_C-(S_C/11)*11) #control number
			A=int(codemeli[9]) #Ragam 10 codemeli
			B=11-C

			if (C==0 and A==C) or (C==1 and A==C) or (C>1 and A==B) :
				b=True
		return b


	def location_codemeli(self,pre_CM):


		if diccode.has_key(pre_CM):
			precode=diccode.get(pre_CM)
			precode1=precode.split(",")
			for i in range(len(precode1)):
				precodemeli=precode1[i]
				t1=threading.Thread(target=self.mkCode,args=(precodemeli,))
				t1.start()
				#t1.join()
				#self.mkCode(precodemeli)


	def __Save(self,filename,data,pre):

		h=open(filename,str(pre))
		h.write(data+"\n")
		h.close()


#---------------------------------------- Function Menu Location Codemeli------------------------------------------------------------------------

def menu_lc():


	if ShowHelpHeader:
		os.system('clear')
		print """
			Generate Location Codemeli

	"""



	input_cm=raw_input(color.get('green')+"For Genrator Location code , Enter location name : "+color.get('end'))
	if input_cm=="back":

		main()
	elif input_cm=="help":
		help()
	elif input_cm=="all":
		save=raw_input("Do You Save CodeMeli to File ? (Y or N) : ")
		if save=="no" or save=="N" or save=="n" or save=="No" :
			for i in range(1000):
				codemeli="%03d" % i
				obj=Codemeli(False)
				t1=threading.Thread(target=obj.mkCode,args=(codemeli,))
				t1.start()
		elif save=="yes" or save=="Y" or save=="y" or save=="Yes" :
			filename=raw_input("Please Enter File name : ")
			for i in range(1000):
				codemeli="%03d" % i
				obj=Codemeli(True,filename)
				t1=threading.Thread(target=obj.mkCode,args=(codemeli,))
				t1.start()


	elif diccode.has_key(input_cm):
		save=raw_input("Do You Save CodeMeli to File ? (Y or N) : ")
		if save=="no" or save=="N" or save=="n" or save=="No" :
			obj=Codemeli(False)
			obj.location_codemeli(input_cm)

		elif save=="yes" or save=="Y" or save=="y" or save=="Yes" :
			filename=raw_input("Please Enter File name : ")
			Fn=Codemeli(True,filename)
			print Fn.location_codemeli(input_cm)

		global ShowHelpHeader
		ShowHelpHeader=False
		menu_lc()

	else :
		print color.get('red')+"\nThe Command Enterd invalid , Please Type help"+color.get('end')
		global ShowHelpHeader
		ShowHelpHeader=False
		menu_lc()




def valid_menu():
	if ShowValidHeader:

		os.system('clear')
		print color.get('red')+"""

			Validation Code Meli


		"""+color.get('end')
	obj=Codemeli(False)
	codemeli=raw_input("Enter the Codemeli : ")
	print obj.validation(codemeli)
	global ShowValidHeader
	ShowValidHeader=False
	valid_menu()

#---------------------------------------- Function help Location Codemeli------------------------------------------------------------------=-------
def help():
	help_table=[["Number","Location","Command"],["1","Iran","all"],["2","Tehran","th"],["3","Zanjan","zn"],["4","khalkhal","kh"]]
	t1_d=DoubleTable(help_table)
	print "\n"+ t1_d.table + "\n"
	global ShowHelpHeader
	ShowHelpHeader=False
	menu_lc()


#---------------------------------------- Function main()----------------------------------------------------------------------------------------
def main():
	os.system('clear')
	if ShowMainHeader:
		print color.get('red')+"""
			Welcome To Codemeli Tools

	Choose of  Items :

		1) Validation Code Meli
		2) Generator Code Meli


	"""+color.get('end')

	try:

		item=int(raw_input(color.get('green')+"Please Enter Items : "+color.get('end')))


		if item==1:
			valid_menu()

		elif item==2:
			menu_lc()
		else :
			print color.get('red')+"item selected incorrect , please type the item exist"+color.get('end')
			raw_input("to contiue press enter ...")
			main()



	except ValueError:
		print "item selected incorrect , please type the item exist "
		raw_input("to contiue press enter ...")
		main()
	except KeyboardInterrupt :
		print "\exit"


main()
