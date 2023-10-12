import tkinter as tk
from tkinter import ttk
import subprocess

# Dictionary of valid usernames and passwords
USERS = {
    "yusuf babatunde": "psc/2019/7593"
}

class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.geometry("400x350")
        master.resizable(False, False)
        master.config(bg="#4d4d4d")

        # Create labels and entries for first name, last name, and password
        self.first_name_label = ttk.Label(master, text="First Name:", font=("Arial", 14), foreground="white", background="#4d4d4d")
        self.first_name_label.pack(pady=(20, 0))
        self.first_name_entry = ttk.Entry(master, font=("Arial", 14))
        self.first_name_entry.pack(pady=(0, 10))

        self.last_name_label = ttk.Label(master, text="Last Name:", font=("Arial", 14), foreground="white", background="#4d4d4d")
        self.last_name_label.pack()
        self.last_name_entry = ttk.Entry(master, font=("Arial", 14))
        self.last_name_entry.pack(pady=(0, 10))

        self.password_label = ttk.Label(master, text="Password:", font=("Arial", 14), foreground="white", background="#4d4d4d")
        self.password_label.pack()
        self.password_entry = ttk.Entry(master, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=(0, 10))

        # Create login button
        self.login_button = ttk.Button(master, text="Login", command=self.login, style="Login.TButton")
        self.login_button.pack(pady=(0, 20))

        # Create style for login button
        style = ttk.Style()
        style.configure("Login.TButton", font=("Arial", 14), foreground="#4d4d4d", background="#d9d9d9")

        # Create footer label
        self.footer_label = ttk.Label(master, text=" Allright reserved © Yusuf Babatunde Yusuf ", font=("Arial", 10), foreground="white", background="#4d4d4d")
        self.footer_label.pack(side="bottom", pady=10)

    def login(self):
        # Get input values
        first_name = self.first_name_entry.get().lower()
        last_name = self.last_name_entry.get().lower()
        password = self.password_entry.get()

        # Check if input values match valid usernames and passwords
        if first_name + " " + last_name in USERS and password.lower() == USERS[first_name + " " + last_name]:
            # Display input values
            ttk.Label(self.master, text=f"Welcome, {first_name.capitalize()} {last_name.capitalize()}!", font=("Arial", 16), foreground="white", background="#4d4d4d").pack(pady=(0, 20))
            
            # Execute SmartC.py file
            subprocess.call(["python", "SmartC.py"])
        else:
            # Display error message
            ttk.Label(self.master, text="Invalid login credentials.", font=("Arial", 14), foreground="red", background="#4d4d4d").pack(pady=(0, 20))

# Create and run GUI
root = tk.Tk()
login_gui = LoginGUI(root)
root.mainloop()
