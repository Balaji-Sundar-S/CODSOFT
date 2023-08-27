import tkinter as tk


def button_click( number ):
	current = entry.get( )
	entry.delete(0, tk.END)
	entry.insert(0, current+str(number))


def button_clear():
	entry.delete(0, tk.END)


def button_remainder():
	current = entry.get( )
	if '%' not in current:
		entry.delete(0, tk.END)
		entry.insert(0, current+'%')


# noinspection PyBroadException
def button_equal():
	try:
		expression = entry.get( ).replace('%', '*0.01')
		result = eval(expression)
		entry.delete(0, tk.END)
		entry.insert(0, result)
	except Exception:
		entry.delete(0, tk.END)
		entry.insert(0, "Error")


root = tk.Tk( )
root.title("Calculator")
root.resizable(False, False)
root.config(bg="#F8F8FF")

entry = tk.Entry(root, width=25, font=('Helvetica', 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
	'7', '8', '9', '/',
	'4', '5', '6', '*',
	'1', '2', '3', '-',
	'0', '.', '+', '%',  # Removed '=' button
]

row_val = 1
col_val = 0
for button in buttons:
	if button == '%':
		tk.Button(root, text=button, padx=21, pady=20, font=('Helvetica', 16),
		          command=button_remainder, bg="#4D4D4D", fg="white").grid(row=row_val, column=col_val)
	elif button == '.':
		tk.Button(root, text=button, padx=28, pady=20, font=('Helvetica', 16),
		          command=lambda b = button: button_click(b), bg="#4D4D4D", fg="white").grid(row=row_val, column=col_val)
	else:
		tk.Button(root, text=button, padx=26, pady=20, font=('Helvetica', 16),
		          command=lambda b = button: button_click(b), bg="#4D4D4D", fg="white").grid(row=row_val, column=col_val)
	col_val += 1
	if col_val > 3:
		col_val = 0
		row_val += 1

tk.Button(root, text="C", padx=24, pady=20, font=('Helvetica', 16), command=button_clear, bg="#007FFF").grid(row=row_val,
					               column=col_val)
col_val += 1

tk.Button(root, text="=", padx=104, pady=20, font=('Helvetica', 16), command=button_equal, bg="#FFB90F").grid(row=row_val,
						column=col_val,
						columnspan=4)

root.mainloop( )
