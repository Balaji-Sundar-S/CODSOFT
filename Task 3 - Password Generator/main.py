import tkinter, random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+' ]

window = tkinter.Tk()
window.title("Password Generator")
window.minsize(width=550, height=400)
window.resizable(False, False)
window.config(bg="light blue")

title = tkinter.Label(text="Password Generator Application", font=("Times New Roman", 20, "bold"), anchor="center")
title.place(x=80, y=0)
title.config(bg="light blue")

passLengthLabel = tkinter.Label(text="Enter Password Length", font=("Times New Roman", 14, "bold"))
passLengthLabel.place(x=170, y=55)
passLengthLabel.config(bg="light blue")

letterLabel = tkinter.Label(text="Letter", font=("Times New Roman", 12, "normal"))
letterLabel.place(x=0, y=100)
letterLabel.config(bg = "light blue")

letterLength = tkinter.Entry(width = 13, font=("Times New Roman", 12, "bold"))
letterLength.place(x=50, y=103)

numberLabel = tkinter.Label(text="Number", font=("Times New Roman", 12, "normal"))
numberLabel.place(x=170, y=100)
numberLabel.config(bg="light blue")

numberLength = tkinter.Entry(width = 13, font=("Times New Roman", 12, "bold"))
numberLength.place(x=240, y=103)

symbolLabel = tkinter.Label(text="Symbols", font=("Times New Roman", 12, "normal"))
symbolLabel.place(x=360, y=100)
symbolLabel.config(bg="light blue")

symbolLength = tkinter.Entry(width = 13, font=("Times New Roman", 12, "bold"))
symbolLength.place(x=430, y=103)


def letter():
	nr_letters = int(letterLength.get( ))
	password1 = ""
	for i in range(nr_letters):
		password1 += random.choice(letters)
	return password1


def number():
	nr_numbers = int(numberLength.get( ))
	password2 = ""
	for i in range(nr_numbers):
		password2 += random.choice(numbers)
	return password2


def symbol():
	nr_symbols = int(symbolLength.get( ))
	password3 = ""
	for i in range(nr_symbols):
		password3 += random.choice(symbols)
	return password3


def fullpassword():
	fpassword = letter() + number() + symbol()
	originalpassword = ''.join(random.sample(fpassword, len(fpassword)))
	return originalpassword
	
	
def generatepassword():
	password.config(text=fullpassword())
	

generate = tkinter.Button(text="Generate", font=("Times New Roman", 16, "bold"), command=generatepassword)
generate.place(x=200, y=155)
generate.config(padx=20, bg="light green")

password = tkinter.Label(width=40, height=2, font=("Times New Roman", 14, "normal"))
password.place(x=70, y=220)


def copypass():
	copy.clipboard_clear()
	copy.clipboard_append(password.cget("text"))
	

copy = tkinter.Button(text="Copy", font=("Times New Roman", 16, "bold"), command=copypass)
copy.place(x=215, y=290)
copy.config(padx=20, bg="light green")

window.mainloop()
