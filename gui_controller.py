import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import controller as cont

switch_state = 'off'

root = tk.Tk()
root.title('TV controller')


#command Switch
def switch():
	global switch_state
	global tv
	global num_label_var
	global set_label_var
	global pict
	global channel_label
	global channels
	#Create TV window
	if switch_state == 'off':
		tv = tk.Toplevel()
		tv.title('TV')
		tv.geometry('700x420+280+190')
		
		
		ch1_im = ImageTk.PhotoImage(Image.open('bbc.png'))
		ch2_im = ImageTk.PhotoImage(Image.open('discovery.png'))
		ch3_im = ImageTk.PhotoImage(Image.open('tv1000.png'))
		no_im = ImageTk.PhotoImage(Image.open('no_ch.png'))
		
		channels = {cont.CHANNELS[0]:ch1_im, cont.CHANNELS[1]:ch2_im, cont.CHANNELS[2]:ch3_im}
		
		channel_label = ttk.Label(tv, text=cont.controller.first_channel())
		channel_label.grid(row=0, column=0)
		
		num_label_var = tk.StringVar()
		num_label_var.set(cont.CHANNELS.index(cont.controller.first_channel())+1)
		num_label = ttk.Label(tv, textvariable=num_label_var)
		num_label.grid(row=0, column=2)
		
		
		window_frame = ttk.Frame(tv, width=700, height=400)
		window_frame.grid(row=1, column=0, columnspan=3, sticky=tk.E)
		
		
		
		pict = tk.Label(window_frame, image=channels[cont.controller.first_channel()])
		pict.grid(row=1)
		
		set_label_var = tk.StringVar()
		set_label = ttk.Label(window_frame, textvariable=set_label_var)
		set_label.grid(row=0)
	
	
		switch_state = 'on'
		tv.mainloop()
	else:
		tv.destroy()
		switch_state = 'off'
		
def num(arg):
	
	set_label_var.set(set_label_var.get() + str(arg))
	
def enter():
	set_label_var.get()
	i = cont.controller.turn_channel(int(set_label_var.get()))
	
	channel_label['text'] = i
	num_label_var.set(cont.CHANNELS.index(i)+1)
	pict['image'] = channels[i]
	set_label_var.set('')
	
def up():
	i = cont.controller.next_channel()
	
	channel_label['text'] = i
	num_label_var.set(cont.CHANNELS.index(i)+1)
	pict['image'] = channels[i]
	
def down():
	i = cont.controller.previous_channel()

	channel_label['text'] = i
	num_label_var.set(cont.CHANNELS.index(i)+1)
	pict['image'] = channels[i]
	
	

#Create frames
frame_num = ttk.Frame(root)
frame_num.grid(row=1, pady=10)

frame_arrow = ttk.Frame(root)
frame_arrow.grid(row=2, sticky=(tk.W, tk.E))

#Create buttons
switch_btn = ttk.Button(root, text='On/Off', command=switch)
switch_btn.grid(row=0, column=0, sticky=tk.W)

btn1 = ttk.Button(frame_num, text='1', command=lambda:num(1))
btn1.grid(row=0, column=0)

btn2 = ttk.Button(frame_num, text='2', command=lambda:num(2))
btn2.grid(row=0, column=1)

btn3 = ttk.Button(frame_num, text='3', command=lambda:num(3))
btn3.grid(row=0, column=2)

btn4 = ttk.Button(frame_num, text='4', command=lambda:num(4))
btn4.grid(row=1, column=0)

btn5 = ttk.Button(frame_num, text='5', command=lambda:num(5))
btn5.grid(row=1, column=1)

btn6 = ttk.Button(frame_num, text='6', command=lambda:num(6))
btn6.grid(row=1, column=2)

btn7 = ttk.Button(frame_num, text='7', command=lambda:num(7))
btn7.grid(row=2, column=0)

btn8 = ttk.Button(frame_num, text='8', command=lambda:num(8))
btn8.grid(row=2, column=1)

btn9 = ttk.Button(frame_num, text='9', command=lambda:num(9))
btn9.grid(row=2, column=2)

btn_zero = ttk.Button(frame_num, text='0', command=lambda:num(0))
btn_zero.grid(row=3, column=1)


btn_up = ttk.Button(frame_arrow, text='\u02C4', command=up)
btn_up.pack(fill=tk.X)

btn_enter = ttk.Button(frame_arrow, text='Enter', command=enter)
btn_enter.pack()

btn_down = ttk.Button(frame_arrow, text='\u02C5', command=down)
btn_down.pack(fill=tk.X)





root.mainloop()
