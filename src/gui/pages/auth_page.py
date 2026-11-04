import customtkinter as ctk


class Auth_Page(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        self.navigation_bar = ctk.CTkFrame(
            self, fg_color="#3c5a9a", height=50, corner_radius=0
        )
        self.navigation_bar.pack(fill="x", pady=0, padx=0)

        for i in range(10):
            self.navigation_bar.columnconfigure(i, minsize=100, weight=1)

        # title
        self.title_label = ctk.CTkLabel(
            self.navigation_bar,
            text="ItsBeeOH",
            font=("Helvetica", 30, "bold"),
        )
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.login_credentials = ctk.CTkFrame(self.navigation_bar, corner_radius=0)
        self.login_credentials.grid(row=0, column=10, sticky="nsew", padx=10, pady=10)

        for i in range(3):
            self.login_credentials.columnconfigure(i, minsize=50, weight=1)

        # login credential inputs
        self.username_entry = ctk.CTkEntry(
            self.login_credentials,
            placeholder_text="Enter username here...",
            font=("Times New Roman", 12),
        )
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_entry = ctk.CTkEntry(
            self.login_credentials,
            placeholder_text="Enter password",
            font=("Times New Roman", 10),
        )
        self.password_entry.grid(row=0, column=2, padx=10, pady=10)

        self.login_btn = ctk.CTkButton(
            self.login_credentials,
            text="Login",
        )

        self.login_btn.grid(row=0, column=3, padx=5, pady=5)

        # self.submit_btn.grid(row=0, column=0, padx=10, pady=10)

        self.hi = ctk.CTkLabel(
            self,
            text="Hi",
            font=("Arial", 18),
            text_color="#2ECC71",
        )
        self.hi.pack(pady=20)
