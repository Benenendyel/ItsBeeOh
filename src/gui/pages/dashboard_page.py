import customtkinter as ctk
from src.data.session import clear_session


class Dashboard_Page(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(self, text="dashboard").pack(pady=20)
        self.logout = ctk.CTkButton(
            self, text="Logout", width=200, height=40, command=self.handle_logout
        )
        self.logout.pack(pady=20)

    def handle_logout(self):
        clear_session()
        self.controller.show_page("Auth_Page")
