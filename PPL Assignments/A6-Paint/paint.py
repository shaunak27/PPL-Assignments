from tkinter import *
from tkinter import ttk, colorchooser
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import *
from PIL import ImageTk, Image
import os
filename = ''
root = Tk()

def title_func():
	for i in range(1000):
		if not os.path.exists('untitled' +str(i) + '.png'):
			filename = 'untitled' +str(i)
			root.title('MyPaint -  ' + 'untitled'+str(i))
			break
    		
	
class main:
    def __init__(self,master):
        self.master = master
        self.pen = 0
        self.eraser = 0
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.penwidth = 4
        self.x = None
        self.y = None
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint) 
        self.c.bind('<ButtonRelease-1>',self.reset)
        

    def paint(self,e):
        if self.x and self.y:
            self.c.create_line(self.x,self.y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.x = e.x
        self.y = e.y

    def reset(self,e):    
        self.x = None
        self.y = None      

    def changeW(self,e): 
        self.penwidth = e
           
    def clear(self):
        self.c.delete(ALL)
        self.color_bg

    def change_fg(self):  
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]
        
    def change_bg(self):  
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        
    def saveas(self):
        fileName = asksaveasfilename()
        self.c.postscript(file = name + '.eps') 
        img = Image.open(name + '.eps') 
        img.save(name + '.png', 'png')
        os.remove(name + '.eps')
    def save(self):
        self.c.postscript(file = filename + '.eps') 
        img = Image.open(filename + '.eps') 
        img.save(filename + '.png', 'png')
        os.remove(filename + '.eps')
    def toggle(self):
    	self.pen = 1 - self.pen
    	self.controlfunc()
    def newfunc(self):
    	if askyesno(title='Warning !', message='Do you want to save this current file ?'):
    		self.saveas()
    		self.clear()
    		title_func()
    	else:
    		self.clear()
    def controlfunc(self):
    	penn = self.pen
    	if(penn):
    		self.controls.pack(side=TOP)
    def erasefunc(self):
    	er = self.eraser
    	if(er):
    		self.color_fg = 'white'
    def etog(self):
    	self.eraser = 1 - self.eraser
    	self.erasefunc()			
    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Size',font=('cooper 24')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
       	self.controlfunc()
        
        self.c = Canvas(self.master,width=500,height=500,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        viewmenu = Menu(menu)
        colormenu = Menu(menu)
        toolmenu = Menu(menu)
        menu.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New',command=self.newfunc)
        filemenu.add_command(label ='Save',command = self.save)
        filemenu.add_command(label ='Save As',command = self.saveas)
        menu.add_cascade(label='Options',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)
        menu.add_cascade(label='View',menu=viewmenu)
        viewmenu.add_command(label='Clear All',command=self.clear)
        viewmenu.add_command(label='Quit',command=self.master.destroy) 
        menu.add_cascade(label = 'Tools',menu=toolmenu)
        toolmenu.add_command(label = 'Set Pen Size',command=self.toggle)
        toolmenu.add_command(label = 'Eraser',command=self.etog)
        
        
        

if __name__ == '__main__':
    
    main(root)
    title_func()
    root.mainloop()
