import ttkbootstrap as ttk
from gooey.examples.res import success
from ttkbootstrap.constants import *

def save_to_file():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get().strip()

    if first_name and last_name and email:
        with open('data.txt', 'a', encoding="utf-8") as file:
            file.write(f'{first_name},{last_name},{email}\n')
        label_status.config(text='Data saved successfully!', bootstyle=SUCCESS)
        entry_first_name.delete(0, 'end')
        entry_last_name.delete(0, 'end')
        entry_email.delete(0, 'end')
    else:
        label_status.config(text='Please fill all fields!', bootstyle=WARNING)

app = ttk.Window(themename='darkly')
app.title('Save Data')
app.geometry('400x300')

label_first_name = ttk.Label(app, text='First Name:')
label_first_name.pack(pady=5)
entry_first_name = ttk.Entry(app, width=30)
entry_first_name.pack(pady=5)

label_last_name = ttk.Label(app, text="Last Name:")
label_last_name.pack(pady=5)
entry_last_name = ttk.Entry(app, width=30)
entry_last_name.pack(pady=5)

label_email = ttk.Label(app, text="Email:")
label_email.pack(pady=5)
entry_email = ttk.Entry(app, width=30)
entry_email.pack(pady=5)

button_save = ttk.Button(app, text='Save', bootstyle=INFO, command=save_to_file)
button_save.pack(pady=20)

label_status = ttk.Label(app, text='', bootstyle=INFO)
label_status.pack(pady=10)

app.mainloop()
