from tkinter import *
from json import load, dump
from tkinter import messagebox, filedialog

def get_info(card_number:str):
    if card_number.endswith('.json'):
        f = open(card_number, 'r')
        data = load(f)
        return data
    else:
        messagebox.showerror("Error", f"Card {card_number} is not a real bank card.")

def enter():
    data = get_info(filedialog.askopenfilename())
    print(data)

    if e_pin.get()==data['pin']:
        manage_window.deiconify()
        root.withdraw()
    else:
        messagebox.showwarning("Warning", f"Wrong pin card {data['cardnumber']}")
config_btn = {
    'bg': 'pink',
    'fg': 'purple',
    'padx': 20,
    'pady': 15,
    'font': ('Times', 20),
}
config_entry = {
    'bg': 'pink',
    'fg': 'purple',
    'font': ('Times', 20),
}
root = Tk()
root.config(bg='pink')
e_pin = Entry(root, cnf=config_entry)
btn_enter = Button(root, text='Enter', cnf=config_btn, command=enter)
manage_window = Toplevel(root)
manage_window.protocol('WM_DELETE_WINDOW', root.destroy)
manage_window.withdraw()
e_pin.pack(padx=15, pady=10)
btn_enter.pack(padx=15, pady=10)
mainloop()