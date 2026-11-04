import customtkinter as ctk
from src.controller.account_controller import create_user, validate_login_credential
from src.data.session import save_session


class Login_Page(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        ctk.CTkLabel(self, text="Login").pack(pady=20)

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter username here...",
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

        self.button_holders = ctk.CTkFrame(self, fg_color="transparent")
        self.button_holders.pack(pady=20, padx=10)

        self.submit_btn = ctk.CTkButton(
            self.button_holders,
            text="Login",
            width=190,
            height=40,
            command=self.handle_submit,
        )
        self.submit_btn.grid(row=0, column=0, padx=10, pady=10)

        self.register_button = ctk.CTkButton(
            self.button_holders,
            text="Create an Account",
            width=190,
            height=40,
            command=lambda: self.controller.show_page("Register_Page"),
        )
        self.register_button.grid(row=0, column=1, padx=10, pady=10)

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
            res = validate_login_credential(username, password)

            if res["success"]:
                self.result_label.configure(text=f"{res['response']}")
                save_session(username)

                self.controller.show_page("Dashboard_Page")
            else:
                self.result_label.configure(text=f"{res['response']}")
        else:
            self.result_label.configure(text="Enter something in both inputs please.")
