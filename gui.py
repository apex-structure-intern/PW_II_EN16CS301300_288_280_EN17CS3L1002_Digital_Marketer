#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 18:35:10 2020

@author: yuvraj
"""

from tkinter import *
from authenticator import *
from PIL import ImageTk, Image
from tkinter import messagebox
from controller import *
from tkinter import filedialog as fd
import tkinter.font as font


class Window:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Social and Email Marketing")
        self.root.geometry("850x500")
        self.main_frame = LabelFrame(self.root, padx = 20, pady = 20)
        self.main_frame.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.login_frame = LabelFrame(self.main_frame, padx = 100, pady = 100)
        self.login_frame.grid(row = 0, column =0, padx = 125, pady = 20 )
        self.control = Controller()
        
    
    def loginpage(self):
        # Declaring variables
        self.user_label = Label(self.login_frame, text = 'Username: ', padx=10, pady = 10)
        self.user_entry = Entry(self.login_frame)
        self.pass_label = Label(self.login_frame, text = 'Password: ', padx=10, pady = 10)
        self.pass_entry = Entry(self.login_frame, show="*")
        self.submit_btn = Button(self.login_frame, text = 'Login', command =self.login, padx = 50, pady = 5)
        self.register_btn = Button(self.login_frame, text ='Register', command = self.registration, padx =40, pady = 5)
         
        # Positioning them:
        self.user_label.grid(row = 0, column = 0, sticky=W)
        self.user_entry.grid(row = 0, column = 1)
        self.pass_label.grid(row = 1, column = 0, sticky=W)
        self.pass_entry.grid(row = 1, column = 1)
        self.submit_btn.grid(row = 2, column = 0, pady = 10, sticky=W)
        self.register_btn.grid(row = 2, column = 1, pady = 10, sticky=W)
        
        
    def registration(self):
        self.top = Toplevel()
        self.top.grab_set()
        self.register_frame = LabelFrame(self.top, padx = 10, pady = 100)
        self.register_frame.grid(row = 0, column =0, padx = 125, pady = 20 )
        
        # Declaring variable
        self.name_label = Label(self.register_frame, text = 'Name: ', pady = 10)
        self.name_entry = Entry(self.register_frame)
        self.username_label = Label(self.register_frame, text = 'Username: ', pady = 10)
        self.username_entry = Entry(self.register_frame)
        self.password_label = Label(self.register_frame, text = 'Password: ', pady = 10)
        self.password_entry = Entry(self.register_frame, show="*")
        self.address_label = Label(self.register_frame, text = 'Address: ', pady = 10)
        self.address_entry = Entry(self.register_frame)
        self.email_label = Label(self.register_frame, text = 'Email: ', pady = 10)
        self.email_entry = Entry(self.register_frame)
        self.number_label = Label(self.register_frame, text = 'Mobile Number: ', pady = 10)
        self.number_entry = Entry(self.register_frame)
        self.submit_btn = Button(self.register_frame, text = "Submit", padx = 10,command = self.regis, pady = 10)
        
        # Positioning them:
        self.name_label.grid(row = 0 , column = 0 , sticky=W)
        self.name_entry.grid(row = 0, column = 1)
        self.username_label.grid(row = 4,column=0, sticky=W)
        self.username_entry.grid(row = 4, column = 1)
        self.password_entry.grid(row = 5, column = 1)
        self.password_label.grid(row = 5,column=0, sticky=W)
        self.address_label.grid(row = 1, column = 0, sticky=W)
        self.address_entry.grid(row = 1, column = 1)
        self.email_label.grid(row = 2, column = 0, sticky=W)
        self.email_entry.grid(row = 2, column = 1)
        self.number_label.grid(row = 3, column = 0, sticky=W)
        self.number_entry.grid(row = 3, column = 1)
        self.submit_btn.grid(row = 6, column = 0, columnspan = 2)
        
    # Login authentication
    def login(self):
        if (authenticate(self.user_entry.get(), self.pass_entry.get()) == True) :
            self.homepage()
        else :
            messagebox.showerror("Incorrect Credentials!!!!","Please enter correct Username and Password!!!")
    
    def regis(self):
        self.lis = [self.name_entry.get(),self.username_entry.get(),self.password_entry.get(),self.address_entry.get(),self.number_entry.get(),self.email_entry.get()]
        if(add_user(*self.lis)):
            messagebox.showinfo("Congrats", "User Created")
            self.top.destroy()
        
    
    def homepage(self):
        # Clearing window
        self.login_frame.destroy()
        self.root.geometry("985x610")
        
        # Creating Frames for every site we want to post our stuff.
        self.insta_frame = LabelFrame(self.main_frame, width = 200, height = 200, text ="Instagram" , padx = 10, pady = 10)
        self.insta_frame.grid(row =0, column =0, padx = 10, pady = 10)
        self.fb_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "Facebook" , padx = 10, pady = 10)
        self.fb_frame.grid(row =0, column =1, padx = 10, pady = 10)
        self.email_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "Email" , padx = 10, pady = 10)
        self.email_frame.grid(row = 1, column =3, padx = 10, pady = 10)
        self.twitter_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "Twitter", padx = 10, pady = 10)
        self.twitter_frame.grid(row =0, column =2, padx = 10, pady = 10)
        self.tumblr_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "Tumblr", padx = 10, pady = 10)
        self.tumblr_frame.grid(row =1, column =0, padx = 10, pady = 10)
        self.myspace_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "MySpace", padx = 10, pady = 10)
        self.myspace_frame.grid(row =1, column =1, padx = 10, pady = 10)
        self.telegram_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "Telegram", padx = 10, pady = 10)
        self.telegram_frame.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.wechat_frame = LabelFrame(self.main_frame, width = 200, height = 200, text = "WeChat", padx = 10, pady = 10)
        self.wechat_frame.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        # Creating buttons with Images of Social Media Sites in them.
        self.buttons = {
            "insta_frame":[self.insta_frame,'logos/insta.png',self.control.insta, 0,0],
            "fb_frame":[self.fb_frame,'logos/fb.png',self.control.fb,0,1],
            "email_frame":[self.email_frame,'logos/email.png',self.control.email,1,3],
            "twitter_frame":[self.twitter_frame, 'logos/twitter.png',self.control.twitter,0,2],
            "tumblr_frame":[self.tumblr_frame, 'logos/tumblr.png',self.control.tumblr,1,0],
            "myspace_frame":[self.myspace_frame, 'logos/myspace.png',self.control.myspace,1,1],
            "telegram_frame":[self.telegram_frame, 'logos/tel.png',self.control.telegram,0,3],
            "wechat_frame":[self.wechat_frame, 'logos/wechat.png',self.control.wechat,1,2]
        }
        
        # Creating Image buttons
        for key, values in self.buttons.items():
            self.buttons[key].append(ImageTk.PhotoImage(Image.open(values[1])))
            Button(values[0], image = self.buttons[key][-1], command=values[2]).pack()
        
        self.post_btn = Button(self.main_frame, text = 'Upload Post', command = self.post_upload)
        self.automate_btn = Button(self.main_frame, text = 'Automate', command = self.automate)
        size = font.Font(size = 20)
        self.post_btn['font'] = size
        self.automate_btn['font'] = size
        self.post_btn.grid(row = 2, column = 1, ipadx = 10)
        self.automate_btn.grid(row = 2, column = 2, ipadx = 25)
        
    def automate(self):
        self.auto_win = Toplevel()
        self.auto_win.grab_set()
        self.auto_frame = LabelFrame(self.auto_win, padx = 10, pady = 10)
        self.auto_frame.grid(row = 0, column =0, padx = 125, pady = 20 )
        
        self.control.automate(self.auto_win,self.auto_frame)
        
       
    def post_upload(self):
        self.post = Toplevel()
        self.post.grab_set()
        self.post_frame = LabelFrame(self.post, padx = 10, pady = 100)
        self.post_frame.grid(row = 0, column =0, padx = 125, pady = 20 )
        
        def upload():
            self.control.path = fd.askopenfile().name
            
        
        def submit():
            self.control.caption = caption_entry.get()
            self.control.hashtags = hashtag_entry.get()
            self.post.destroy()
        
        caption_lbl = Label(self.post_frame, text="Enter Caption", padx = 10)
        caption_entry = Entry(self.post_frame)
        hashtag_lbl = Label(self.post_frame, text="Enter Hashtags", padx = 10)
        hashtag_entry = Entry(self.post_frame)
        upload_btn = Button(self.post_frame, text = 'Select Image', command = upload)
        submit_btn = Button(self.post_frame, text = 'Submit', command = submit)
        
        caption_lbl.grid(row = 0, column = 0)
        caption_entry.grid(row = 0, column = 1)
        hashtag_lbl.grid(row = 1, column = 0)
        hashtag_entry.grid(row = 1, column = 1)
        upload_btn.grid(row=2, column = 0, columnspan=2)
        submit_btn.grid(row = 4, column = 0, columnspan = 2)
        
        
if __name__ == "__main__":
    root = Tk()
    new = Window(root)
    new.loginpage()
    root.mainloop()
