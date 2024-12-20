from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("vihanga's text editor")
window.geometry("600x500")
window. rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(0,minsize=800,weight=1)
def open_file():
    x=askopenfilename(filetypes=[("textfiles","*.txt"),("allfiles","*.*")])
    if not X:
     return
    txt_edit.delete(1.0,END)
    with open(x,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title("vihanga's text editor")
def save_file():
    x=askopenfilename(defaultextension="txt",filetypes=[("Text Files","*.txt*"),("All files","*.*")])
    if not x:
        return
    with open(x,"w")as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title("vihanga's text editor")
    
txt_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="open",command=open_file)
btn_save=Button(fr_button,text="save as",command=save_file)    
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0, sticky="ew",padx=5) 
fr_button.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="NSEW") 
window.mainloop()  
    