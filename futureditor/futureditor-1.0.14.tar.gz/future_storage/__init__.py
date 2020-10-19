#!/usr/bin/python
from tkinter import *
import os
import sys
import subprocess
import webbrowser
import pyperclip as pc
import json
from tkinter import colorchooser

try:
	with open("user_settings","r") as read_file:
		d = json.load(read_file)
		colour = d["bg"]
		colour2 = d["fg"]
		_font_ = d["font"]
		font_size = d["font_size"]
		cursor = d["cursor"]
except:
	colour = "white"
	colour2 = "black"
	font_size = 18
	_font_ = "avenir"
	cursor = "True"

try:
	read_file =  open("future-editor-cache.py","r")
	x = read_file.read()
	read_file.close()
	if x == "":
		x = "Hello there type code here to run"
except:
	x = "Hello there type code here to run"

def future_editor(colour=colour,colour2=colour2,font_size=font_size,_font_=_font_,text=x,_cursor_=cursor):

	#styling of the button and textbox is given here
	font= _font_
	font_size_ = font_size

	data = {
	"font":font,
	"font_size":font_size_,
	"bg":colour,
	"fg":colour2,
	"cursor":_cursor_
	}

	with open("user_settings","w") as write_file:
		json.dump(data,write_file)

	with open("user_settings","r") as read_file:
		global d
		d = json.load(read_file)

	bg=colour
	fg=colour2

	#takes the code from the text-box and saves it as a file using python in usrs/ directory
	global i
	i = 0

	def show_colour(for_bg=False,for_fg=False):
		colour = colorchooser.askcolor()[1]
		print(colour)
		if colour == "":
			pass
		else:
			if for_bg == True:
				text_colour.delete(0,"end")
				text_colour.insert(0,colour)
			elif for_fg == True:
				text_colour_1.delete(0,"end")
				text_colour_1.insert(0,colour)

	def change_colour(colour,colour2,font,font_size,cursor):
		bg = colour
		fg = colour2
		window.destroy()
		try:
			future_editor(colour,colour2,font_size=font_size,_font_ = font,_cursor_=cursor)
		except:
			print("You did not enter a valid colour/font try relaunching the editor")
	def run_code():
		code_given = str(code.get("1.0",'end-1c'))
		create_file =  open("future-editor-cache.py","w+")
		create_file.write(code_given)
		create_file.close()
		try:
			os.system("python future-editor-cache.py")
		except:
			print("Your system does not have python in its system variable.")
	def copy_():
		code_given = str(code.get("1.0",'end-1c'))
		try:
			subprocess.run("pbcopy", universal_newlines=True, input=code_given)
		except:
			pc.copy(code_given)

	def clear_():
		code.delete("1.0","end")

	def theme_():
		window_theme = Toplevel()
		window_theme.title("Theme")
		window_theme.config(bg=bg)

		label_window = Label(window_theme,bg=bg,fg=fg,font=font,text="Colour of window")
		label_window.grid(row=0,column=0,columnspan=2)

		global text_colour
		text_colour = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		text_colour.grid(row=1,column=0,columnspan=1)
		try:
			text_colour.insert(0,d["bg"])
		except:
			text_colour.insert(0,"white")

		show_colours = Button(window_theme,bg="white",fg="black",font=font,command=lambda: show_colour(for_bg=True),text="show colours")
		show_colours.grid(row=1,column=1,pady=10)

		label_font = Label(window_theme,bg=bg,fg=fg,font=font,text="Colour of Text")
		label_font.grid(row=2,column=0,columnspan=2)

		global text_colour_1
		text_colour_1 = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		text_colour_1.grid(row=3,column=0,columnspan=1)
		try:
			text_colour_1.insert(0,d["fg"])
		except:
			text_colour_1.insert(0,"black")
		
		show_colours = Button(window_theme,bg="white",fg="black",font=font,command=lambda: show_colour(for_fg=True),text="show colours")
		show_colours.grid(row=3,column=1,pady=10)


		label_font_ = Label(window_theme,bg=bg,fg=fg,font=font,text="Font and Font size")
		label_font_.grid(row=4,column=0,columnspan=2)

		font_ = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		font_.grid(row=5,column=0,columnspan=2,sticky=W+E)
		try:
			font_.insert(0,d["font"])
		except:
			font_.insert(0,"avenir")

		_font_size_ = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		_font_size_.grid(row=6,column=0,columnspan=2,sticky=W+E)
		try:
			_font_size_.insert(0,d["font_size"])
		except:
			_font_size_.insert(0,"20")

		cursor = Label(window_theme,text="Block cursor",bg=bg,fg=fg,font=font)
		cursor.grid(row=7,column=0)

		cursor_ = Entry(window_theme,bg=bg,fg=fg,font=font)
		cursor_.grid(row=7,column=1)
		try:
			cursor_.insert(0,d["cursor"])
		except:
			cursor_.insert(0,"True")

		apply_button = Button(window_theme,bg="white",fg="black",font=font,command = lambda: change_colour(str(text_colour.get()),str(text_colour_1.get()),str(font_.get()),int(_font_size_.get()),str(cursor_.get())),text="Apply")
		apply_button.grid(row=8,column=0,pady=10,columnspan=2)


	window = Tk()
	window.title("Future-editor")

	scrollbar = Scrollbar(window)
	scrollbar.grid(row=1,column=5,sticky=N+S)

	code = Text(window,bg=bg,fg=fg,insertbackground=fg,font=(font,font_size_),undo=True,blockcursor=True,yscrollcommand = scrollbar.set)
	code.grid(row=1,column=0,columnspan=5)
	code.insert(END,text)


	if _cursor_ == "True":
		code.config(blockcursor=True)
	elif _cursor_ == "False":
		code.config(blockcursor=False)

	scrollbar.config( command = code.yview )

	run = Button(window,bg="white",fg="black",command=run_code,font=font,text="Run")
	run.grid(row=2,column=0,columnspan=6,sticky=W+E)

	copy_code = Button(window,bg="white",fg="black",command=copy_,font=font,text="copy code")
	copy_code.grid(row=0,column=0,sticky=W+E)

	theme_code = Button(window,bg="white",fg="black",command=theme_,font=font,text="Theme")
	theme_code.grid(row=0,column=2,sticky=W+E)

	delete_code = Button(window,bg="white",fg="black",command=clear_,font=font,text="clear code")
	delete_code.grid(row=0,column=1,sticky=W+E)

	redo_code = Button(window,bg="white",fg="black",command=code.edit_redo,font=font,text="redo")
	redo_code.grid(row=0,column=3,sticky=W+E)

	undo_code = Button(window,bg="white",fg="black",command=code.edit_undo,font=font,text="undo")
	undo_code.grid(row=0,column=4,columnspan=2,sticky=W+E)

	window.mainloop()

if __name__=='__main__':
	try:
		future_editor()
	except:
		print("Theme ERROR: you did not enter a valid theme last time, try changing it now and restart the app")
		future_editor(colour="black",colour2="white",font_size=20,_font_="avenir")
