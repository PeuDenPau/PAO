
from tkinter import *
import tkinter.messagebox
import random
import pickle
import os
from xlrd import open_workbook

class menu:
	def __init__(self,master):
		self.master=master
		master.title("PAO Trainer")
		self.bigFrame=Frame(master)
		self.trainingButton=Button(self.bigFrame,text="TRAINING",command=lambda:self.training())
		self.marathonButton=Button(self.bigFrame,text="MARATHON",command=lambda:self.marathon())

		#layout
		self.bigFrame.grid()
		self.trainingButton.grid(row=0,column=0,padx=50,pady=50)
		self.trainingButton.config(font=("Calibri",30))

		self.marathonButton.grid(row=0,column=1,padx=50,pady=50)
		self.marathonButton.config(font=("Calibri",30))

		self.check_Exel()

	def training(self):
		self.bigFrame.grid_forget()
		entreno99(root)

	def marathon(self):
		self.bigFrame.grid_forget()
		marathon(root)

	def check_Exel(self):
		if os.path.isfile('PAO.kbb'):
			pass
		elif os.path.isfile('PAO.xlsx'):
			for f in os.listdir('.'):
				os.rename(f, f.replace('PAO.xlsx', 'PAO.kbb')) 
		else:
			tkinter.messagebox.showerror("ERROR: NOT PAO FILE DETECTED","You should put the PAO.xlsx with the correct format in the same directory you are running this program. \n\nI will close now. Greetings!")
			root.destroy()

class marathon:
	def __init__(self,master):
		self.master=master
		master.title("PAO Marathon")
		self.bigFrame=Frame(master)
		self.excel = open_workbook('PAO.kbb')

		self.array=[]
		self.MAX=100
		self.in_Bucle=True
		self.first_Click = True

		for i in range(self.MAX):
			self.array= self.array+[i]
		
		self.P_Num=random.randint(0,99)
		self.A_Num=random.randint(0,99)
		self.O_Num=random.randint(0,99)

		self.P_Num_Text=IntVar()
		self.A_Num_Text=IntVar()
		self.O_Num_Text=IntVar()

		self.P_Num_Text.set(format(self.P_Num,'02d'))
		self.A_Num_Text.set(format(self.A_Num,'02d'))
		self.O_Num_Text.set(format(self.O_Num,'02d'))	


		self.P_Label = Label(self.bigFrame,textvariable=self.P_Num_Text)	

		self.A_Label = Label(self.bigFrame,textvariable=self.A_Num_Text)

		self.O_Label = Label(self.bigFrame,textvariable=self.O_Num_Text)

		self.next_Button=Button(self.bigFrame,text="NEXT",width= 40,command=lambda:self.next())	
		self.hint_Button=Button(self.bigFrame,text="HINT",command=lambda:self.show_Hint())

		self.Play_Button= Button(self.bigFrame, text="PLAY",command=lambda:self.play1())
		self.Stop_Button= Button(self.bigFrame, text="STOP",command=lambda:self.stop())

		self.counter_Field=Entry(self.bigFrame)
		self.counter_Field.insert(1,'Time in miliseconds...')
		self.counter_Field.bind('<FocusIn>', self.on_entry_click)


		#LAYOUT
		self.bigFrame.grid()
		self.P_Label.grid(row=0,column=0, pady=20,padx=20, sticky=S+N+E+W)
		self.P_Label.config(font=("Calibri",20))	

		self.A_Label.grid(row=0,column=1, pady=20,padx=20, sticky=S+N+E+W)
		self.A_Label.config(font=("Calibri",20))	

		self.O_Label.grid(row=0,column=2, pady=20,padx=20, sticky=S+N+E+W)
		self.O_Label.config(font=("Calibri",20))	

		self.next_Button.grid(row=2,column=0 ,columnspan=3, padx=20,)
		self.hint_Button.grid(row=3,column=0,pady=10)
		self.Play_Button.grid(row=3,column=2)

		self.counter_Field.grid(row=3,column=1)


	def on_entry_click(self,event):

	    if self.first_Click: # if this is the first time they clicked it
	        first_Click = False
	        self.counter_Field.delete(0, "end") # delete all the text in the entry

	def next(self):
		self.P_Num=random.randint(0,99)
		self.A_Num=random.randint(0,99)
		self.O_Num=random.randint(0,99)

		self.P_Num_Text.set(format(self.P_Num,'02d'))
		self.A_Num_Text.set(format(self.A_Num,'02d'))
		self.O_Num_Text.set(format(self.O_Num,'02d'))		
		try:
			self.hint_lbl_A.destroy()
			self.hint_lbl_P.destroy()
			self.hint_lbl_O.destroy()
		except:
			pass

	def show_Hint(self):
		try:
			self.hint_lbl_A.destroy()
			self.hint_lbl_P.destroy()
			self.hint_lbl_O.destroy()
		except:
			pass
			
		self.hint_lbl_num_P = IntVar()
		self.hint_lbl_num_A = IntVar()
		self.hint_lbl_num_O = IntVar()

		for s in self.excel.sheets():
			self.hint_lbl_num_P.set(s.cell(self.P_Num,0).value)
			self.hint_lbl_num_A.set(s.cell(self.A_Num,1).value)
			self.hint_lbl_num_O.set(s.cell(self.O_Num,2).value)

		self.hint_lbl_P = Label(self.bigFrame,textvariable=self.hint_lbl_num_P)
		self.hint_lbl_A = Label(self.bigFrame,textvariable=self.hint_lbl_num_A)
		self.hint_lbl_O = Label(self.bigFrame,textvariable=self.hint_lbl_num_O)

		
		self.hint_lbl_P.grid(row=1, column=0, pady=10,padx=5,sticky= S)
		self.hint_lbl_A.grid(row=1, column=1, pady=10,padx=5,sticky= S)
		self.hint_lbl_O.grid(row=1, column=2, pady=10,padx=5,sticky= S)

	def play1(self):
		self.in_Bucle=True
		self.play()

	def play(self):
		if self.in_Bucle == True:
			print(isinstance(self.counter_Field.get(),long))
			if  isinstance(self.counter_Field.get(),int)==True:
				self.Play_Button.grid_forget()
				self.Stop_Button.grid(row=3,column=2)
				self.next()
				root.after(self.counter_Field.get(), self.play)
			else:
				tkinter.messagebox.showerror("ERROR", "You should enter a miliseconds time for the interval. Try again!")

	def stop(self):
		self.Stop_Button.grid_forget()
		self.Play_Button.grid(row=3,column=2)
		self.in_Bucle=False

class entreno99:
	def __init__(self,master):
		self.master=master
		master.title("PAO Trainer")

		self.array=[]
		self.easy=[]
		self.medium=[]
		self.hard=[]
		self.MAX=100
		self.excel = open_workbook('PAO.kbb')

		for i in range(self.MAX):
		 	self.array  = self.array + [i]
		random.shuffle(self.array)

		
		self.total_label_text = IntVar()
		self.total_label_text.set(format(self.array[0],'02d'))
		self.total_label = Label(master,textvariable=self.total_label_text)

		self.counter_label_num = IntVar()
		self.counter_label_num.set(len(self.array))
		self.counter_label = Label(master,textvariable=self.counter_label_num)

		#dropList
		self.choices = ['Person', 'Action', 'Object']
		self.PAO = StringVar()
		self.PAO.set('Person')
		self.dropList = OptionMenu(master, self.PAO, *self.choices)


		self.saveButton=Button(master,text="Save",command=lambda:self.saveData())
		self.showHintButton=Button(master,text="Show hint",command=lambda:self.showHint())
		self.showArraysButton=Button(master,text="Show state",command=lambda:self.showInf())
		self.easyButton=Button(master,text="EASY",command=lambda:self.update("easy"))
		self.mediumButton=Button(master,text="MEDIUM",command=lambda:self.update("medium"))
		self.hardButton=Button(master,text="HARD",command=lambda:self.update("hard"))

		#LAYOUT

		self.total_label.grid(row=1, column=0, pady=10,padx=5,columnspan = 3,sticky=S+W+E+N)
		self.total_label.config(font=("Courier", 44))

		self.counter_label.grid(row=0, column=2, pady=10,padx=5,sticky=E+N)

		self.dropList.grid(row=0,column=1)

		self.saveButton.grid(row=0,column=2, pady=10,padx=30)

		self.showHintButton.grid(row=1, column=0, pady=10,padx=5,sticky= S)

		self.showArraysButton.grid(row=0,column=0, pady=10,padx=10)
		self.easyButton.grid(row=10, column=0, pady=10,padx=10,sticky=S+W+E+N)
		self.easyButton.config(font=("Calibri", 20, "bold"))
		self.mediumButton.grid(row=10, column=1, pady=10,padx=10,sticky=S+W+E+N)
		self.mediumButton.config(font=("Calibri", 20,"bold"))
		self.hardButton.grid(row=10, column=2, pady=10,padx=10,sticky=S+W+E+N)
		self.hardButton.config(font=("Calibri", 20,"bold"))

		self.loadData()

	def update(self, method):

		if len(self.array)==0:
			self.informe()


		if method == "easy":
			self.easy= self.easy+[self.array[0]]

		if method == "medium":
			self.medium= self.medium+[self.array[0]]

		if method == "hard":
			self.hard= self.hard+[self.array[0]]

		self.array.pop(0)

		if len(self.array)==0:
			self.informe()

		self.total_label_text.set(format(self.array[0],'02d'))
		self.counter_label_num.set(len(self.array))
		try:
			self.hint_lbl.destroy()
		except:
			pass


	def showHint(self):
		try:
			self.hint_lbl.destroy()
		except:
			pass
			
		if self.PAO.get() =='Person': 
			var=0
		elif self.PAO.get() =='Action': 
			var=1
		else: 
			var=2

		self.hint_lbl_num = IntVar()
		for s in self.excel.sheets():
			self.hint_lbl_num.set(s.cell(self.array[0],var).value)
		self.hint_lbl = Label(self.master,textvariable=self.hint_lbl_num)

		self.hint_lbl.grid(row=1, column=2, pady=10,padx=5,sticky= S)


	def informe(self):
		validacion= tkinter.messagebox.askquestion('Resultados','EASY= '+str(self.easy)+
																'\n\nMEDIUM= '+str(self.medium)+
																'\n\nHARD= '+str(self.hard)+
																'\n\n\nAnother round?')
		if validacion=='yes':
			self.MAX=len(self.hard)
			self.array=self.hard
			self.hard=self.medium
			self.medium=self.easy
			self.easy=[]
			random.shuffle(self.array)


		if validacion=='no':
			self.save= tkinter.messagebox.askquestion("Save","Do you want to save state for future trainings?")

			root.quit()

	def showInf(self):
		tkinter.messagebox.showinfo('Information','TO DO= '+str(self.array)+
											'\n\nHARD= '+str(self.hard)+
											'\n\nMEDIUM= '+str(self.medium)+
											'\n\nEASY= '+str(self.easy))

	def saveData(self):
		if os.path.isfile('data.kbb'):
			os.remove("data.kbb")
		with open("data.kbb", "wb") as f:   #Pickling
			pickle.dump((self.array,self.easy,self.medium,self.hard), f)
		tkinter.messagebox.showinfo("Saved", "Succesfully saved!")

	def loadData(self):
		if os.path.isfile('data.kbb'):
			load= tkinter.messagebox.askquestion("Load","Do you want to load state from previous training?")
			if load=='yes':
				with open("data.kbb","rb")as f:
					self.array,self.easy,self.medium,self.hard=pickle.load(f)
				self.total_label_text.set(format(self.array[0],'02d'))
		self.counter_label_num.set(len(self.array))


root = Tk()
marathon(root)
root.mainloop()  
