import tkinter as tk
import tkinter.font as tkFont

def poStisku():
    global lbl_hodn

    lbl_hodn.set("Ok")




okno=tk.Tk()
okno.geometry("800x600")
velky_font = tkFont.Font(family="Arail", size=30)

lbl_hodn=tk.StringVar(value="AA")
lbl_hodn2=tk.StringVar(value="BB")

lbl1=tk.Label(okno,font=velky_font,textvariable=lbl_hodn)
lbl1.grid(row=2,column=0)

lbl2=tk.Label(okno,textvariable=lbl_hodn2,font=velky_font)
lbl2.grid(row=0,column=2)

txtbox=tk.Entry(okno,font=velky_font)
txtbox.grid(row=0,column=1)

btn=tk.Button(okno,text="stiskni",command=poStisku,font=velky_font)
btn.grid(row=2,column=1)

okno.mainloop()




