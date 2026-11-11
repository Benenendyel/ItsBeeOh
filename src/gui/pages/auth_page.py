import customtkinter as ctk
from src.controller.account_controller import create_user, validate_login_credential
from src.data.session import save_session
from PIL import Image
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


class Auth_Page(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        ###################################################
        # navigation part
        ###################################################

        self.navigation_bar = ctk.CTkFrame(
            self, fg_color="#3c5a9a", height=50, corner_radius=0
        )
        self.navigation_bar.pack(fill="x", pady=0, padx=0)

        self.navigation_bar.columnconfigure(0, weight=0)
        self.navigation_bar.columnconfigure(1, weight=1)
        self.navigation_bar.columnconfigure(2, weight=0)

        # title
        self.title_label = ctk.CTkLabel(
            self.navigation_bar,
            text="ItsBeeOH",
            font=("Helvetica", 30, "bold"),
        )
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.login_credentials = ctk.CTkFrame(
            self.navigation_bar, corner_radius=0, fg_color="transparent"
        )
        self.login_credentials.grid(row=0, column=10, sticky="nsew", padx=10, pady=10)

        for i in range(3):
            self.login_credentials.columnconfigure(i, weight=1)

        # login credential inputs
        self.username_entry = ctk.CTkEntry(
            self.login_credentials,
            placeholder_text="Enter username here...",
            font=("Arial", 11),
            fg_color="white",
            text_color="black",
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
        )
        self.username_entry.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = ctk.CTkEntry(
            self.login_credentials,
            placeholder_text="Enter password",
            font=("Arial", 11),
            fg_color="white",
            text_color="black",
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
            show="●",
        )
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        self.login_btn = ctk.CTkButton(
            self.login_credentials,
            text="Login",
            width=60,
            fg_color="#496aaf",
            font=("Arial", 11, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
            command=self.handle_submit,
        )
        self.login_btn.grid(row=0, column=2, padx=5, pady=5)

        ###################################################
        # registration part
        ###################################################

        self.register_credentials = ctk.CTkFrame(self, fg_color="transparent")

        self.register_credentials.pack(fill="both", expand=True, pady=50, padx=100)

        self.register_credentials.rowconfigure(0, weight=1)
        self.register_credentials.columnconfigure(0, weight=1)
        self.register_credentials.columnconfigure(1, weight=0)
        self.register_credentials.columnconfigure(2, weight=0)

        self.header = ctk.CTkFrame(self.register_credentials, fg_color="transparent")
        self.header.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        self.text = ctk.CTkLabel(
            self.header,
            text="ItsBeeOh helps you find what kind of movies you watch in your life.",
            font=("Arial", 21, "bold"),
            wraplength=400,
            justify="left",
            text_color="#3c5a9a",
        )
        self.text.grid(row=0, column=0, padx=10, pady=10)

        self.header_image = ctk.CTkImage(
            light_image=Image.open(ASSETS / "HeaderImage.png"),
            size=(400, 200),
        )

        self.image_label = ctk.CTkLabel(self.header, image=self.header_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.register_form = ctk.CTkFrame(
            self.register_credentials,
            fg_color="transparent",
        )
        self.register_form.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.register_form.rowconfigure(0, weight=0)
        self.register_form.rowconfigure(1, weight=0)
        self.register_form.rowconfigure(2, weight=0)
        self.register_form.rowconfigure(3, weight=0)

        self.register_form_label = ctk.CTkLabel(
            self.register_form,
            text="Create an Account",
            font=("Arial", 21, "bold"),
            wraplength=400,
            justify="left",
            text_color="black",
        )

        self.register_form_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.create_username = ctk.CTkEntry(
            self.register_form,
            placeholder_text="Enter username here...",
            font=("Arial", 12),
            fg_color="white",
            text_color="black",
            width=250,
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
        )

        self.create_username.grid(row=1, column=0, padx=10, pady=10)

        self.create_password = ctk.CTkEntry(
            self.register_form,
            placeholder_text="Create a password here...",
            font=("Arial", 12),
            fg_color="white",
            text_color="black",
            width=250,
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
        )

        self.create_password.grid(row=2, column=0, padx=10, pady=10)

        self.register_button = ctk.CTkButton(
            self.register_form,
            text="Sign Up",
            width=100,
            fg_color="#008001",
            font=("Arial", 14, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#2b2b2b",
            command=self.handle_register,
        )

        self.register_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.register_status = ctk.CTkLabel(
            self.register_form,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=400,
            justify="left",
            text_color="black",
        )

        self.register_status.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def handle_submit(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            res = validate_login_credential(username, password)

            if res["success"]:
                self.register_status.configure(text=f"{res['response']}")
                save_session(username)

                self.controller.show_page("Dashboard_Page")
            else:
                self.register_status.configure(text=f"{res['response']}")
        else:
            self.register_status.configure(
                text="Enter something in both inputs please."
            )

    def handle_register(self):
        username = self.create_username.get().strip()
        password = self.create_password.get().strip()

        if username and password:
            res = create_user(username, password)

            if res["success"]:
                self.register_status.configure(
                    text=f"{res['response']}", text_color="green"
                )
            else:
                self.register_status.configure(
                    text=f"{res['response']}", text_color="orange"
                )
        else:
            self.register_status.configure(
                text="Enter something in both inputs please.", text_color="red"
            )
