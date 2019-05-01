# coding: utf-8

import sys
import tkinter as tk
import subprocess

def helloworld():
    command = ['ls', '-l']
    subprocess.call(command)

def main():
    root = tk.Tk()
    root.title(u"Test Tools")
    root.geometry("400x300")

    button = tk.Button(root, text="Dockerrun", command=helloworld)
    button.grid()

    root.mainloop()

if __name__ == '__main__': main()
