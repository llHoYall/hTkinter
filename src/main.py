import customtkinter

from ui import SettingsUI


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("hTkinter")
        self.minsize(480, 320)

        self._init_ui()

    def reset_ui(self, color_theme: str) -> None:
        self.settings.destroy()
        self.tabview.destroy()
        self._init_ui(color_theme)

    def _init_ui(self, color_theme: str = "Default") -> None:
        # --- Frame --- #
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.add("Settings")

        # --- Component --- #
        self.settings = SettingsUI(self.tabview.tab("Settings"), self, color_theme)

        # --- Layout --- #
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)
        self.settings.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
