#!/usr/bin/python
from tkinter import *
import os
import sys
import time
import datetime
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
except:
	colour = "black"
	colour2 = "white"
	font_size = 18
	_font_ = "avenir"


def future_editor(colour=colour,colour2=colour2,font_size=font_size,_font_=_font_):

	#styling of the button and textbox is given here
	font= _font_
	font_size_ = font_size

	data = {
	"font":font,
	"font_size":font_size_,
	"bg":colour,
	"fg":colour2
	}

	with open("user_settings","w") as write_file:
		json.dump(data,write_file)

	bg=colour
	fg=colour2

	#takes the code from the text-box and saves it as a file using python in usrs/ directory
	global i
	i = 0

	def show_colour(for_bg=False,for_fg=False):
		colour = colorchooser.askcolor()[1]
		if for_bg == True:
			text_colour.delete(0,"end")
			text_colour.insert(0,colour)
		elif for_fg == True:
			text_colour_1.delete(0,"end")
			text_colour_1.insert(0,colour)


	def t_c():
		path = os.path.join(os.path.dirname(__file__),"terms_and_conditions.html")
		f = open(path,'w')

		message = """
<!DOCTYPE html>
<html>
<head>
	<title>Future-editor</title>
	<style>
		.head{
			color: "black";
			text-decoration: underline red;
			float: center;
		}
		.para{
			margin-left: 100px;
			margin-right: 100px;
			margin-top: 100px;
			margin-bottom: 100px;
			box-sizing: 10px 10px 10px 10px;
			box-shadow: 5px 10px 18px #888888;
			font-family: "courier";
			font-size: 25px;
			transition-duration: 0.5s;
		}
		.para:hover{
			transform: scale(1.1);
		}
		.button{
			background-color: black;
			border: none;
			color: white;
			padding: 35px;
			text-align: center;
			text-decoration: none;
			font-size: 16px;
			margin: 4px 600px;
			cursor: pointer;
			border-radius: 12px;
			transition-duration: 0s;

		}
		.button:hover{
			color: #111;
            background: #39ff14;
            box-shadow: 0 0 50px #39ff14;
		}
	</style>
</head>
<body>
	<div style="clear: both">
		<h1 class= "head">
			TERMS OF CONDITIONS
		</h1>
	</div>
	<hr />
	<p class= "para">
		MIT License

	Copyright (c) [2020] [Future-editor]

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.
	<br>
	<br>
	<B>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.
	</B>
	</p>
	<button class="button" onclick="closeit()">AGREE AND EXIT</button>
	<script>
	function closeit(){
		close()
	}
	</script>
</body>
</html>

		"""

		f.write(message)
		f.close()

		#Change path to reflect file location
		webbrowser.open("file://"+path)

	def change_colour(colour,colour2,font,font_size):
		bg = colour
		fg = colour2
		window.destroy()
		try:
			future_editor(colour,colour2,font_size=font_size,_font_ = font)
		except:
			print("You did not enter a valid colour/font try relaunching the editor")
	def run_code():
		code_given = str(code.get("1.0",'end-1c'))
		date = str(datetime.datetime.now())
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
		text_colour.insert(0,"black")

		show_colours = Button(window_theme,bg="white",fg="black",font=font,command=lambda: show_colour(for_bg=True),text="show colours")
		show_colours.grid(row=1,column=1,pady=10)

		label_font = Label(window_theme,bg=bg,fg=fg,font=font,text="Colour of Text")
		label_font.grid(row=2,column=0,columnspan=2)

		global text_colour_1
		text_colour_1 = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		text_colour_1.grid(row=3,column=0,columnspan=1)
		text_colour_1.insert(0,"white")
		
		show_colours = Button(window_theme,bg="white",fg="black",font=font,command=lambda: show_colour(for_fg=True),text="show colours")
		show_colours.grid(row=3,column=1,pady=10)


		label_font_ = Label(window_theme,bg=bg,fg=fg,font=font,text="Font and Font size")
		label_font_.grid(row=4,column=0,columnspan=2)

		font_ = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		font_.grid(row=5,column=0,columnspan=2,sticky=W+E)
		font_.insert(0,"avenir")

		_font_size_ = Entry(window_theme,bg=bg,fg=fg,insertbackground=fg,font=font)
		_font_size_.grid(row=6,column=0,columnspan=2,sticky=W+E)
		_font_size_.insert(0,"20")


		apply_button = Button(window_theme,bg="white",fg="black",font=font,command = lambda: change_colour(str(text_colour.get()),str(text_colour_1.get()),str(font_.get()),int(_font_size_.get())),text="Apply")
		apply_button.grid(row=7,column=0,pady=10,columnspan=2)


	window = Tk()
	window.title("Future-editor")

	code = Text(window,bg=bg,fg=fg,insertbackground=fg,font=(font,font_size_),undo=True)
	code.grid(row=1,column=0,columnspan=4)

	run = Button(window,bg="white",fg="black",command=run_code,font=font,text="Run")
	run.grid(row=2,column=0,columnspan=4,sticky=W+E)

	copy_code = Button(window,bg="white",fg="black",command=copy_,font=font,text="copy code")
	copy_code.grid(row=0,column=0,sticky=W+E)

	theme_code = Button(window,bg="white",fg="black",command=theme_,font=font,text="Theme")
	theme_code.grid(row=0,column=2,sticky=W+E)

	terms = Button(window,bg="white",fg="black",command=t_c,font=font,text="Terms & Conditons")
	terms.grid(row=0,column=3,sticky=W+E)

	delete_code = Button(window,bg="white",fg="black",command=clear_,font=font,text="clear code")
	delete_code.grid(row=0,column=1,sticky=W+E)


	window.mainloop()

if __name__=='__main__':
	try:
		future_editor()
	except:
		print("Theme ERROR: you did not enter a valid theme last time, try changing it now and restart the app")
		future_editor(colour="black",colour2="white",font_size=20,_font_="avenir")
