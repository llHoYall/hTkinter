from typing import Any

import tkinter
import customtkinter

from util import convert_path


class SettingsUI(customtkinter.CTkFrame):
    def __init__(self, parent: Any, app: Any, color_theme: str) -> None:
        super().__init__(parent)

        # --- Variable --- #
        self._app = app

        self._mode_var = tkinter.StringVar()
        self._mode_var.set(self._get_appearance_mode())

        self._color_var = tkinter.StringVar()
        self._color_var.set(color_theme)

        # --- Widget --- #
        frame = customtkinter.CTkFrame(self)
        mode_label = customtkinter.CTkLabel(
            frame,
            text="Select Mode",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.mode_switch = customtkinter.CTkSwitch(
            frame,
            text=self._get_appearance_mode().capitalize(),
            variable=self._mode_var,
            onvalue="dark",
            offvalue="light",
            command=self._change_mode,
        )

        color_label = customtkinter.CTkLabel(
            frame,
            text="Select Color",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.color_opt = customtkinter.CTkOptionMenu(
            frame,
            values=["Default", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"],
            variable=self._color_var,
            command=self._change_color,
        )

        # --- Layout --- #
        frame.grid(row=0, padx=10, pady=10)
        mode_label.grid(row=0, column=0, padx=15, pady=10)
        self.mode_switch.grid(row=0, column=1, padx=15, sticky="e")
        color_label.grid(row=1, column=0, padx=15)
        self.color_opt.grid(row=1, column=1, padx=10, pady=10)

    def _change_mode(self) -> None:
        customtkinter.set_appearance_mode(self._mode_var.get())
        self.mode_switch.configure(text=self._mode_var.get().capitalize())

    def _change_color(self, choice) -> None:
        customtkinter.set_default_color_theme(convert_path(f"./resource/{choice}.json"))
        self._app.reset_ui(choice)
