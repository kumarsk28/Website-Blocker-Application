from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import sys
import os
website_list = []
website=" "        
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def show_data():
    site= var_chk.get()   
    if site == 1:
        website="www.facebook.com"
        website_list.append(website)
    elif site == 2:
        website="www.twitter.com"
        website_list.append(website)
    elif site == 3:
        website="www.youtube.com"
        website_list.append(website)
    elif site == 4:
        website="locksicker.com"
        website_list.append(website)
    elif site == 5:
        website="www.instagram.com"
        website_list.append(website)
    elif site == 6:
        website="www.skype.com"
        website_list.append(website)
    tkinter.messagebox.showinfo("Message","Website Added Sucessfully")
        
def block():
    with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list: 
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
                tkinter.messagebox.showinfo("Message","Website Blocked Sucessfully")
def unblock():
     with open(hosts_path, 'r+') as file:
                content = file.readlines() 
                file.seek(0) 
                for line in content:
                    if not any(website in line for website in website_list): 
                        file.write(line)
                    file.truncate()
                tkinter.messagebox.showinfo("Message","Fun hours ... Enjoy")

def helloCallBck():
    os.system('python project2.py')
    
def about():
    tkinter.messagebox.showinfo("About"," Site Blocker App \n Designed In Python \n Suggestions Are Welcomed")

def bye():
         root.destroy();

def reach():
    tkinter.messagebox.showinfo("Contact Us","Puja : bhard.puja@gmail.com\nSiddharth : aadarsh.siddharth@gmail.com\nShubham : 94727shubham@gmail.com")

root = Tk()
root.geometry("850x700")
root.title("SiteBlockingApp")
root.iconbitmap(r'blocker.ico')
var_chk = IntVar()

'''background_img = PhotoImage(file = "image2.png")'''
background_lb = Label (root, bg='black')
background_lb.place(x=0, y =0, relheight=1, relwidth=1)

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="About",command=about)
submenu.add_separator()
submenu.add_command(label="Exit",command=bye)

menu.add_cascade(label="Reach Us",command=reach)


label_0 = Label(root, text="Website  Blocker",width=15,font=("bold", 50) , bg ="black", fg="yellow")
label_0.place(x=135,y=45)
l1 = Label(root, text=" List of Website(select 1 at a time) :", bg="black", fg="white", width=30,font=("bold", 20) )
l1.place(x=165,y=180)
l2 = Label(root, text="What do you want?", bg="black", fg="white",width=25,font=("bold", 20))
l2.place(x=190, y=450)

ch1= Radiobutton(root, text="Facebook", variable=var_chk, value=1 ,width=8,fg='white',bg='black',font=("bold",12))
ch1.place(x=280,y=240)
photo1 = PhotoImage(file='facebook.png')
labelphoto = Label(root, image= photo1)
labelphoto.place(x=380, y=240)
ch2= Radiobutton(root, text="Twitter ", variable=var_chk, value=2, width=8,fg='white',bg='black', font=("bold",12))
ch2.place(x=430,y=240)
photo2 = PhotoImage(file='twitter.png')
labelphoto = Label(root, image= photo2)
labelphoto.place(x=530, y=240)
ch3= Radiobutton(root, text="Youtube ", variable=var_chk, value=3, width=8,fg='white',bg='black',font=("bold",12))
ch3.place(x=280,y=280)
photo3 = PhotoImage(file='youtube.png')
labelphoto = Label(root, image= photo3)
labelphoto.place(x=380, y=280)
ch4= Radiobutton(root, text="Locksicker", variable=var_chk, value=4 , width=8,fg='white',bg='black',font=("bold",12))
ch4.place(x=430,y=280)
photo4 = PhotoImage(file='locked.png')
labelphoto = Label(root, image= photo4)
labelphoto.place(x=530, y=280)
ch5= Radiobutton(root, text="Instagram", variable=var_chk, value=5 , width=8,fg='white',bg='black',font=("bold",12))
ch5.place(x=280,y=320)
photo5 = PhotoImage(file='instagram.png')
labelphoto = Label(root, image= photo5)
labelphoto.place(x=380, y=320)
ch6= Radiobutton(root, text="Skype", variable=var_chk, value=6 , width=8,fg='white',bg='black',font=("bold",12))
ch6.place(x=430,y=320)
photo6 = PhotoImage(file='skype.png')
labelphoto = Label(root, image= photo6)
labelphoto.place(x=530, y=320)
ch7= Button(root, text="Submit " ,width=8,font=("bold",12),fg='green',command=show_data)
ch7.place(x=380,y=400)
ch8= Button(root, text="Block ",width=8,font=("bold",12),fg='red',bg='black', command=block )
ch8.place(x=280,y=530)
ch9= Button(root, text="Unblock " ,width=8, font=("bold",12), fg='green',bg='black',command=unblock) 
ch9.place(x=430,y=530)
ch10= Button(root, text="Other... ",width=8, font=("bold",12),command=helloCallBck )
ch10.place(x=680,y=400)

root.mainloop()
