import tkinter as tk
from tkinter import ttk, messagebox as msg


A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"


# 主窗口
class Window(tk.Tk):
	def __init__(self):
		super().__init__()

		self.width = 400
		self.height = 150
		self.screenwidth = self.winfo_screenwidth()
		self.screenheight = self.winfo_screenheight()
		self.x = (self.screenwidth - self.width) / 2
		self.y = (self.screenheight - self.height) / 2
		self.size = "%dx%d+%d+%d" % (self.width, self.height, self.x, self.y)
		self.geometry(self.size)
		self.resizable(False, False)

		self.title("DCT(Decimal Conversion Tool) by Lonely-Pea")


# 主界面
class Application(tk.Frame):
	def __init__(self, master):
		super().__init__(master)

		self.master = master

		self.place(x=0, y=0, width=400, height=300)

		self.var_1 = tk.StringVar()
		self.var_2 = tk.StringVar()

		self.decimals = ["2进制", "8进制", "10进制", "16进制"]
		self.var_1.set(self.decimals[0])
		self.var_2.set(self.decimals[2])

		self.entry_var1 = tk.IntVar()
		self.entry_var2 = tk.IntVar()

		self.desktop()

	def desktop(self):
		combobox1 = ttk.Combobox(self, textvariable=self.var_1, value=self.decimals, state="readonly")
		combobox1.place(x=15, y=15, width=135, height=25)

		combobox2 = ttk.Combobox(self, textvariable=self.var_2, value=self.decimals, state="readonly")
		combobox2.place(x=250, y=15, width=135, height=25)

		label1 = tk.Label(self, text="->")
		label1.place(x=150, y=15, width=100, height=25)

		entry1 = ttk.Entry(self, textvariable=self.entry_var1)
		entry1.place(x=15, y=55, width=135, height=25)

		entry2 = ttk.Entry(self, textvariable=self.entry_var2, state="readonly")
		entry2.place(x=250, y=55, width=135, height=25)

		button1 = ttk.Button(self, text="开始转化", command=self.conversion)
		button1.place(x=165, y=55, width=70, height=25)

		label2 = tk.Label(self, text="DCT(Decimal Conversion Tool) Created by Lonely-Pea", anchor="w")
		label2.place(x=15, y=110, width=400, height=25)

	def conversion(self):
		text_var_1 = self.var_1.get()
		text_entry_var_1 = self.entry_var1.get()
		text_length = len(str(int(text_entry_var_1)))

		text_var_2 = self.var_2.get()

		# print(int(str(text_var_1[0:len(text_var_1)-2])))

		# 转化为10进制
		decimal10_number = self.conversion_to_decimal10(decimal=int(str(text_var_1[0:len(text_var_1)-2])), text_length=text_length, text=text_entry_var_1)

		#　10进制转化为目标进制
		decimal_result_number = self.conversion_decimal10_to_result(decimal10_number=decimal10_number, result_decimal=int(str(text_var_2[0:len(text_var_2)-2])))

		# 显示结果
		self.entry_var2.set(decimal_result_number)

		# print(decimal10_number)
		# print(decimal_result_number)
	
	def conversion_to_decimal10(self, decimal: int, text_length: int, text: str):  # 转化为10进制
		decimal10_number = 0  # 十进制式子

		if decimal == 2:  #　２进制转化
			decimal2_lst = []

			for index in range(0, text_length):
				decimal2_lst.append(int(str(text)[index])*(2**(text_length-index-1)))

			for number in decimal2_lst:
				decimal10_number += number

		if decimal == 8:  #　八进制转化
			decimal8_lst = []

			for index in range(0, text_length):
				decimal8_lst.append(int(str(text)[index])*(8**(text_length-index-1)))

			for number in decimal8_lst:
				decimal10_number += number

		if decimal == 10:  # 十进制转化
			decimal10_number += int(text)

		if decimal == 16:  # 十六进制转化
			decimal16_lst = []

			for index in range(0, text_length):
				index_text = 0

				if text[index] in [A, B, C, D, E, F]:
					if text[index] == A:
						index_text = 10
					elif text[index] == B:
						index_text = 11
					elif text[index] == C:
						index_text = 12
					elif text[index] == D:
						index_text = 13
					elif text[index] == E:
						index_text = 14
					else:
						index_text = 15		

				else:
					index_text = int(text[index])
					
				decimal16_lst.append(int(index_text)*(16**(text_length-index-1)))
				
			for number in decimal16_lst:
				decimal10_number += number

		return decimal10_number

	def conversion_decimal10_to_result(self, decimal10_number: int, result_decimal: int):  #　将十进制转化为目标进制
		result_decimal_number = ""  #　目标进制式子
		decimal10_number = decimal10_number
		remainder_number_lst = []

		if result_decimal == 2:  #　转化为2进制
			while decimal10_number != 0:
				remainder_number  = decimal10_number - decimal10_number // 2
				remainder_number_lst.append(remainder_number)
				decimal10_number = decimal10_number // 2
				continue

		elif result_decimal == 8:  # 转化为8进制
			while decimal10_number != 0:
				remainder_number = decimal10_number - decimal10_number // 8
				remainder_number_lst.append(remainder_number)
				decimal10_number = decimal10_number // 2
				continue

		elif result_decimal == 10:  # 转化为10进制
			remainder_number_lst.append(decimal10_number)

		else:  # 转化为16进制
			while decimal10_number != 0:
				remainder_number = decimal10_number - decimal10_number // 16
				if remainder_number in [10, 11, 12, 13, 14, 15]:
					if remainder_number == 10:
						remainder_number_lst.append(A)
					elif remainder_number_lst == 11:
						remainder_number_lst.append(B)
					elif remainder_number_lst == 12:
						remainder_number_lst.append(C)
					elif remainder_number_lst == 13:
						remainder_number_lst.append(D)
					elif remainder_number_lst == 14:
						remainder_number_lst.append(E)
					else:
						remainder_number_lst.append(F)
				else:
					remainder_number_lst.append(remainder_number)

				decimal10_number = decimal10_number // 16
				continue

		for index in range(0, len(remainder_number_lst)):  # 拼接
			result_decimal_number += str(remainder_number_lst[len(remainder_number_lst)-index-1])

		return result_decimal_number


# 测试
if __name__ == "__main__":
	window = Window()
	application = Application(master=window)

	window.mainloop()
