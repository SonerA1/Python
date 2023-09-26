import base64
import tkinter
from tkinter import messagebox, END
from PIL import ImageTk, Image
import os

FONT = ("Verdena", 20, "normal")
window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

# ui


img = ImageTk.PhotoImage(Image.open("secret.jpg"))
panel = tkinter.Label(window, image=img)
panel.pack(side="top", fill="both", expand="yes")

title_info = tkinter.Label(text="Enter your title", font=FONT)
title_info.pack()

title_info_entry = tkinter.Entry(width=50)
title_info_entry.pack()

secret_input = tkinter.Label(text="Enter your Secret", font=FONT)
secret_input.pack()

secret_input_text = tkinter.Text(width=50, height=25)
secret_input_text.pack()

master_key_input = tkinter.Label(text="Enter master key", font=FONT)
master_key_input.pack()

master_key_entry = tkinter.Entry(width=50)
master_key_entry.pack()

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i])+ ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr(256 + ord(enc[i]) - ord(key_c) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_button_selected():
    title = title_info_entry.get()
    message = secret_input_text.get("1.0", END)
    master_secret = master_key_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info")
    else:
        #encryption
        message_encrypted = encode(master_secret,message)
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write((f"\n{title}\n{message_encrypted}"))
        finally:
            title_info_entry.delete(0,END)
            master_key_entry.delete(0,END)
            secret_input_text.delete("1.0",END)

def dep_button_selected():
    message_encrypted = secret_input_text.get("1.0",END)
    master_secret = master_key_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            secret_input_text.delete("1.0",END)
            secret_input_text.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please enter encrypted text!")




save_button = tkinter.Button(text="Save & Encrytp", command=save_button_selected)
save_button.pack()


dep_button = tkinter.Button(text="Depcryt", command=dep_button_selected)
dep_button.pack()

window.mainloop()
