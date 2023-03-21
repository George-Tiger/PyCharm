# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@contact:   shendan1986@126.com
@file:  Form.py
@time:  2023/3/17
@desc:  登录
@author: George
"""
import tkinter
from tkinter import *
from dataclasses import dataclass


@dataclass
class Loginform:
    master: Tk
    user_entry: [Entry]
    pwd_entry: [Entry]

    def create_widgets(self):
        """
        构造窗体界面
        """
        user_label = Label(self.master, text='用户名', fg='blue')
        user_label.grid(row=0, column=0)
        self.user_entry = Entry(self.master)
        self.user_entry.grid(row=0, column=1)

        pwd_label = Label(self.master, text='密码', fg='blue')
        pwd_label.grid(row=1, column=0)
        self.pwd_entry = Entry(self.master)
        self.pwd_entry.grid(row=1, column=1)

        btn_login = Button(self.master, text='登录', font=14, fg='yellow', bg='green', padx=15,
                           command=self.login)
        btn_login.grid(row=2, column=0)

        btn_reset = Button(self.master, text='重置', font=14, fg='yellow', bg='green', padx=15,
                           command=self.reset)
        btn_reset.grid(row=2, column=1)

    def login(self):
        """
        登录验证
        """
        name = self.user_entry.get()
        pwd = self.pwd_entry.get()
        if name == 'admin' and pwd == 'admin':
            print('welcome to my app,dear' + name)
        else:
            print('your information is error!')

    def reset(self):
        """
        重置文本框
        """
        self.user_entry.delete(0, END)
        self.pwd_entry.delete(0, END)

    def run(self):
        self.create_widgets()
        self.master.geometry('200x300')
        self.master.wm_title('登录')
        self.master.mainloop()


root = Tk()
userLogin = Loginform(root, Entry, Entry)
userLogin.run()

"""
生成文档
"""
# if __name__ == "__main__":
#     import Form
#
#     print
#     help(Form)
