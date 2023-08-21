import tkinter

window = tkinter.Tk()
window.title("To Do List")
window.minsize(800, 610)
window.resizable(False, False)
window.config(bg="light blue")
pointer = 0

title = tkinter.Label(text="To Do List Application", font=("monotype corsiva", 24, "bold"), anchor="center")
title.place(x=240, y=0)
title.config(bg="light blue")

todo = tkinter.Listbox(height=22, width=35, bd=3, selectmode='multiple')
todo.place(x=400, y=70)
todo.config(font=("Times New Roman", 16, "italic"))

taskLabel = tkinter.Label(text="Enter the task :", font=("Times New Roman", 18, "bold"))
taskLabel.place(x=40, y=150)
taskLabel.config(bg="light blue")

task = tkinter.Entry(width=30, font=("Times New Roman", 16, "normal"))
task.place(x=40, y=190)


def add():
	global pointer
	pointer += 1
	todo.insert(pointer, task.get())
	task.option_clear()
	task.delete(0, "end")
	

addtask = tkinter.Button(text="Add Task", font=("Times New Roman", 16, "normal"), command=add)
addtask.place(x=40, y=240)
addtask.config(padx=120)


def delete():
	global pointer
	selected = todo.curselection()
	for selectedtask in selected[::-1]:
		todo.delete(selectedtask)
	pointer -= 1
	

deletetask = tkinter.Button(text="Delete Task", font=("Times New Roman", 16, "normal"), command=delete)
deletetask.place(x=40, y=300)
deletetask.config(padx=110)


def deletealltask():
	global pointer
	todo.delete(0, "end")
	pointer = 0
	

deleteall = tkinter.Button(text="Delete All", font=("Times New Roman", 16, "normal"), command=deletealltask)
deleteall.place(x=40, y=360)
deleteall.config(padx=117)

window.mainloop()
