# Wechat, Telegram, edit needed!!!

import sys
# Adding local path files
sys.path.insert(1, '/home/yuvraj/Desktop/apexstructures/Digital_marketing/social_media')
sys.path.insert(2, '/home/yuvraj/Desktop/apexstructures/Digital_marketing/auto_email')

from mass_mail import *
from main import Obj
from tkinter import messagebox, Button
from tkinter.ttk import Progressbar
import time

class Controller:
    caption = ''
    hashtags = ''
    path = ''
    def __init__(self):
        self.social = Obj()
        self.mailer = MassMail()
        
    def fb(self):
        if (self.social.fb.upload_post(self.caption, self.path)) :
            messagebox.showinfo("Done!!!","Your Posts has been upload!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def insta(self):
        if (self.social.insta.upload_post(self.caption, self.path)) :
            messagebox.showinfo("Done!!!","Your Posts has been upload!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def tumblr(self):
        if (self.social.tumblr.upload_post(self.caption, self.path)) :
            messagebox.showinfo("Done!!!","Your Posts has been upload!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def twitter(self):
        if (self.social.twitter.upload_post(self.caption, self.path)) :
            messagebox.showinfo("Done!!!","Your Posts has been upload!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def myspace(self):
        if (self.social.myspace.upload_post()) :
            messagebox.showinfo("Done!!!","Your Posts has been upload!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def telegram(self):
        # pass parameters here
        #return self.social.tel.broadcast(params)
        if (False) :
            messagebox.showinfo("Done!!!","Your Message is Broadcast!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
        
    
    def wechat(self):
        # Edit needed
        if (False) :
            messagebox.showinfo("Done!!!","Your Message is Broadcast!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def email(self):
        if (mailer.broadcast()) :
            messagebox.showinfo("Done!!!")
        else :
            messagebox.showerror("Error!!","Try Again. After Sometime!!!")
    
    def automate(self,auto_win, auto_frame):
        def cancel():
            auto_win.destroy()
            return 0
        progress = Progressbar(auto_frame, length = 100, mode = 'determinate')
        progress.grid(row = 0, column =0, pady = 10, ipadx = 100)
        cancel_btn = Button(auto_frame, text = "Cancel", command = cancel)
        cancel_btn.grid(row = 1, column = 0)
        progress['value'] = 1
        auto_frame.update_idletasks()
        #self.fb()
        progress['value'] = 5
        auto_frame.update_idletasks() 
        time.sleep(2.0)
        #self.twitter()
        progress['value'] = 10
        auto_frame.update_idletasks() 
        time.sleep(2.0)
        #self.myspace()
        progress['value'] = 20
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        #self.telegram()
        progress['value'] = 40
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        print("still running!!!")
        #self.email()
        progress['value'] = 60
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        #self.wechat()
        progress['value'] = 80
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        #self.tumblr()
        progress['value'] = 85
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        #self.insta()
        progress['value'] = 100
        auto_frame.update_idletasks() 
        time.sleep(0.5)
        
        cancel()
        #time.sleep(3600)
        
    
