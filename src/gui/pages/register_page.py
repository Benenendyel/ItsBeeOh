import customtkinter as ctk
from src.controller.account_controller import create_user


class Register_Page(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        ctk.CTkLabel(self, text="Regitrration page na to").pack(pady=20)

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Type your name here...",
            width=400,
            height=45,
            font=("Arial", 14),
        )
        self.username_entry.pack(pady=20)

        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter password",
            width=400,
            height=45,
            font=("Arial", 14),
        )
        self.password_entry.pack(pady=20)

        self.submit_btn = ctk.CTkButton(
            self, text="Register", width=200, height=40, command=self.handle_submit
        )
        self.submit_btn.pack(pady=10)

        self.submit_btn = ctk.CTkButton(
            self,
            text="I have an account",
            width=200,
            height=40,
            command=lambda: self.controller.show_page("Login_Page"),
        )
        self.submit_btn.pack(pady=10)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18),
            text_color="#2ECC71",
        )
        self.result_label.pack(pady=20)

    def handle_submit(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            res = create_user(username, password)

            if res["success"]:
                self.result_label.configure(text=f"{res['response']}")
            else:
                self.result_label.configure(text=f"{res['response']}")
        else:
            self.result_label.configure(text="Enter something in both inputs please.")
