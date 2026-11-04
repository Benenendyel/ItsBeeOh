import customtkinter as ctk
from src.data.session import check_session
from src.gui.pages.login_page import Login_Page
from src.gui.pages.register_page import Register_Page
from src.gui.pages.dashboard_page import Dashboard_Page
from src.gui.pages.auth_page import Auth_Page


# the whole gui window
class Window(ctk.CTk):
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("ItsBeeOh")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

        container = ctk.CTkFrame(self, fg_color="#f5f6fa")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for Page in (Login_Page, Register_Page, Dashboard_Page, Auth_Page):
            page = Page(container, self)
            self.pages[Page.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        if check_session():
            self.show_page("Auth_Page")
        else:
            self.show_page("Dashboard_Page")

    def show_page(self, frame):
        self.pages[frame].tkraise()
