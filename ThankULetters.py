import csv

from docx import Document
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def read_csv_file(button_text):
    path = filedialog.askopenfilename()
    data = []
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


def letter299(data):
    letter = Document()
    


def button_clicked(button_text):
    data = read_csv_file(button_text)
    if button_text == 'up to 299':
        return letter299(data)

    if button_text == 'Press sign letters':
        return letterPress(data)

    if button_text == '50th anniversary':
        return letter50(data)

    if button_text == 'in honor':
        return letterHonor(data)

    if button_text == 'in memory':
        return letterMem(data)

def create_button(button_text, window):
    return tk.Button(window, text=button_text, command=lambda: button_clicked(button_text))


def creat_gui():
    window = tk.Tk()
    window.title('Hi Kristina! What type of letter are we writing today?')

    button1 = create_button('up to 299', window)
    button1.pack(pady=5)

    button2 = create_button('Press sign letters', window)
    button2.pack(pady=5)

    button3 = create_button('50th anniversary', window)
    button3.pack(pady=5)

    button4 = create_button('in honor', window)
    button4.pack(pady=5)

    button5 = create_button('in memory', window)
    button5.pack(pady=5)

    window.mainloop()


def main():
    creat_gui()


main()
