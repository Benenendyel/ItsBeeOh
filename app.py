from src.gui.window import Window
from src.data.db import init_db
from src.data.session import init_session, clear_session
import src.data.api


def main():

    # # initialize database
    app = Window()
    app.mainloop()


if __name__ == "__main__":
    main()
