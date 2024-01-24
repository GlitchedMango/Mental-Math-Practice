import customtkinter

class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Settings Gui
        self.app = app
        self.geometry("350x350")
        self.title("Settings")

        self.frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.settings_label = customtkinter.CTkLabel(self.frame, text="Settings")
        self.settings_label.grid(row=0, column=0,columnspan=3, padx=40, pady=10)

        self.min_max_label = customtkinter.CTkLabel(self.frame, text="Min                      Max", text_color="gray")
        self.min_max_label.grid(row=1, column=1,columnspan=2, padx=0, pady=10)

        self.plus_switch = customtkinter.CTkSwitch(self.frame, text="+", width=50,command=lambda: self.app.toggle_operation("+", self.plus_switch.get()))
        self.plus_switch.grid(row=2, column=0, padx=20, pady=10)
        self.plus_switch.select()

        self.plus_min_entry = customtkinter.CTkEntry(self.frame, placeholder_text="1", width=50)
        self.plus_min_entry.grid(row=2, column=1, padx=10, pady=10)

        self.plus_max_entry = customtkinter.CTkEntry(self.frame, placeholder_text="100", width=50)
        self.plus_max_entry.grid(row=2, column=2, padx=10, pady=10)

        self.minus_switch = customtkinter.CTkSwitch(self.frame, text="-", width=50, command=lambda: self.app.toggle_operation("-", self.minus_switch.get()))
        self.minus_switch.grid(row=3, column=0, padx=20, pady=10)
        self.minus_switch.select()

        self.minus_min_entry = customtkinter.CTkEntry(self.frame, placeholder_text="1", width=50)
        self.minus_min_entry.grid(row=3, column=1, padx=10, pady=10)

        self.minus_max_entry = customtkinter.CTkEntry(self.frame, placeholder_text="100", width=50)
        self.minus_max_entry.grid(row=3, column=2, padx=10, pady=10)

        self.multiply_switch = customtkinter.CTkSwitch(self.frame, text="*", width=50, command=lambda: self.app.toggle_operation("*", self.multiply_switch.get()))
        self.multiply_switch.grid(row=4, column=0, padx=20, pady=10)
        self.multiply_switch.select()

        self.multiply_min_entry = customtkinter.CTkEntry(self.frame, placeholder_text="1", width=50)
        self.multiply_min_entry.grid(row=4, column=1, padx=10, pady=10)

        self.multiply_max_entry = customtkinter.CTkEntry(self.frame, placeholder_text="20", width=50)
        self.multiply_max_entry.grid(row=4, column=2, padx=10, pady=10)

        self.apply_button = customtkinter.CTkButton(self.frame, text="Apply", command=self.app.apply_settings, fg_color="#738080", text_color="black", hover_color="#738080")
        self.apply_button.grid(row=5, column=1, columnspan=2, padx=20, pady=10)