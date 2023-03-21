# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time     : 2023/3/20 16:16
@Author   : George
@FileName : Translation.py
@Software : PyCharm
"""

import requests
from requests.exceptions import RequestException as RE
import tkinter as tk
from dataclasses import dataclass


@dataclass
class Translation:
    form: None
    form_input: tk.Entry
    form_info: tk.Text
    form_translation: tk.Button
    form_clear_input: tk.Button
    form_clear_output: tk.Button

    def form_init(self):
        master = self.form
        master.title("Translation")
        master.resizable(0, 0)
        self.form_input = tk.Entry(width=80)
        self.form_info = tk.Text(height=18)
        self.form_translation = tk.Button(text='翻译', relief=tk.RAISED, width=8, height=1, command=self.fanyi)
        self.form_clear_input = tk.Button(text='清空输入', relief=tk.RAISED, width=8, height=1,
                                          command=self.clear_input)
        self.form_clear_output = tk.Button(text='清空输出', relief=tk.RAISED, width=8, height=1,
                                           command=self.clear_info)

        self.form_input.grid(row=0, sticky="W", padx=1)
        self.form_info.grid(row=1)
        self.form_translation.grid(row=0, column=1, padx=2)
        self.form_clear_input.grid(row=0, column=2, padx=2)
        self.form_clear_output.grid(row=0, column=3, padx=2)
        master.mainloop()

    def fanyi(self):
        origin = self.form_input.get()
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': origin
        }
        url = "http://fanyi.youdao.com/translate"

        try:
            r = requests.get(url, params=data)
            if r.status_code == 200:
                result = r.json()
                translate_result = result['translateResult'][0][0]["tgt"]
                self.form_info.delete(1.0, "end")
                self.form_info.insert('end', translate_result)
        except RE:
            self.form_info.insert('end', "发送错误")

    def clear_info(self):
        self.form_info.delete(1.0, "end")

    def clear_input(self):
        self.form_input.delete(0, "end")


def main():
    t = Translation(tk.Tk(), None, None, None, None, None)
    t.form_init()


if __name__ == '__main__':
    main()
