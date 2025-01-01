from ttkbootstrap import Style, Window
from tkinter import messagebox, ttk

DATA_FILE = "users.txt"
def save_to_file(data):
    with open(DATA_FILE, "a") as file:
        file.write(data + "\n")

def load_from_file():
    with open(DATA_FILE, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

class MultiPageApp:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.style = Style(theme="superhero")
        self.init_description()

    def switch_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def init_description(self):
        frame = ttk.Frame(self.root, padding=20)
        ttk.Label(frame,text="Welcome to the MultiPage App",font=("Arial Black", 20, "bold"),anchor="center").pack(pady=20)

        ttk.Label(frame,text="This application helps you register, set up your password, and log in securely.",font=("Arial", 12),anchor="center").pack(pady=10)

        ttk.Button( frame,text="Get Started",style="danger.TButton",command=self.init_page1 ).pack(pady=30)
        self.switch_frame(frame)

    def init_page1(self):
        frame = ttk.Frame(self.root, padding=20)
        ttk.Label(frame, text="First Name", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        first_name = ttk.Entry(frame, font=("Arial", 12))
        first_name.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Last Name", font=("Arial", 14)).grid(row=1, column=0, pady=5)
        last_name = ttk.Entry(frame, font=("Arial", 12))
        last_name.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Email", font=("Arial", 14)).grid(row=2, column=0, pady=5)
        email = ttk.Entry(frame, font=("Arial", 12))
        email.grid(row=2, column=1, pady=5)

        ttk.Button(frame, text="Next", style="danger.TButton", command=lambda: self.init_page2(first_name.get(), last_name.get(), email.get())).grid(row=3, columnspan=2, pady=15)
        self.switch_frame(frame)

    def init_page2(self, first_name, last_name, email):
        frame = ttk.Frame(self.root, padding=20)
        ttk.Label(frame, text="Password", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        password = ttk.Entry(frame, show="*", font=("Arial", 12))
        password.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Confirm Password", font=("Arial", 14)).grid(row=1, column=0, pady=5)
        confirm_password = ttk.Entry(frame, show="*", font=("Arial", 12))
        confirm_password.grid(row=1, column=1, pady=5)

        ttk.Button(frame, text="Back", style="secondary.TButton", command=self.init_description).grid(row=2, column=0, pady=15)
        ttk.Button(frame, text="Submit", style="success.TButton", command=lambda: self.submit_data(first_name, last_name, email, password.get(), confirm_password.get())).grid(row=2, column=1, pady=15)
        self.switch_frame(frame)

    def init_page3(self):
        frame = ttk.Frame(self.root, padding=20)
        ttk.Label(frame, text="Email", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        email = ttk.Entry(frame, font=("Arial", 12))
        email.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Password", font=("Arial", 14)).grid(row=1, column=0, pady=5)
        password = ttk.Entry(frame, show="*", font=("Arial", 12))
        password.grid(row=1, column=1, pady=5)

        ttk.Button(frame, text="Login", style="primary.TButton", command=lambda: self.login_user(email.get(), password.get())).grid(row=2, columnspan=2, pady=15)
        self.switch_frame(frame)

    def submit_data(self, first_name, last_name, email, password, confirm_password):
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        existing_users = load_from_file()
        if any(user[2] == email for user in existing_users):
            messagebox.showerror("Error", "Email already exists")
            return

        save_to_file(f"{first_name},{last_name},{email},{password}")
        messagebox.showinfo("Success", "User registered successfully!")
        self.init_page3()

    def login_user(self, email, password):
        existing_users = load_from_file()
        if any(user[2] == email and user[3] == password for user in existing_users):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid email or password")

if __name__ == "__main__":
    root = Window(themename="superhero")
    app = MultiPageApp(root)
    root.mainloop()
