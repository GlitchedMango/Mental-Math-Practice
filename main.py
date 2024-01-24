import customtkinter    
import random
import settings

class App:
    def __init__(self):
        #  Main GUI
        self.app = customtkinter.CTk()
        self.app.geometry("350x300")
        self.app.title("Mental Math Practice")

        self.frame = customtkinter.CTkFrame(self.app, corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = customtkinter.CTkLabel(self.frame, text="Mental Math Practice")
        self.title_label.grid(row=0, column=0,columnspan=4, padx=40, pady=20)

        self.dummy_label = customtkinter.CTkLabel(self.frame, text="")
        self.dummy_label.grid(row=1, column=0, padx=20)

        self.dummy_label1 = customtkinter.CTkLabel(self.frame, text="")
        self.dummy_label1.grid(row=1, column=3, padx=20)

        self.math_label = customtkinter.CTkLabel(self.frame, text="0 + 0 = ")
        self.math_label.grid(row=1, column=1, padx=0, pady=00)

        self.entry_label = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_label.grid(row=1, column=2, padx=0, pady=00)

        self.score_label = customtkinter.CTkLabel(self.frame, text="Score: 0", text_color="gray", width=20)
        self.score_label.grid(row=2, column=0,columnspan=4, padx=40, pady=20)

        self.settings_button = customtkinter.CTkButton(self.frame, text="Settings", command=self.open_settings, fg_color="#738080", text_color="black", hover_color="#738080")
        self.settings_button.grid(row=3, column=0, columnspan=4, padx=40, pady=20)

        # Variables

        self.data = {
            "score": 0,
            "plus_numbers": list(range(1, 101)),
            "minus_numbers": list(range(1, 101)),
            "multiply_numbers": list(range(1, 21)),
            "operations": {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y},
            "outcome": 0
        }

        self.OPERATIONS = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y
        }

        self.settings_window = None

    # Functions

# Opens the settings window
    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = settings.SettingsWindow(self, self.app)
        else:
            self.settings_window.focus()

# Removes and appends the operation to make them 
# interactable by create_calculation
    def toggle_operation(self, operation, value):
        if value == 1:
            self.data["operations"][operation] = self.OPERATIONS[operation]
        else:
            del self.data["operations"][operation]

# Checks if the settings are intigers and min < max, then applies them
    def apply_settings(self): 
        entries = [
            ("plus", self.settings_window.plus_min_entry, self.settings_window.plus_max_entry),
            ("minus", self.settings_window.minus_min_entry, self.settings_window.minus_max_entry),
            ("multiply", self.settings_window.multiply_min_entry, self.settings_window.multiply_max_entry)
        ]

        for name, min_entry, max_entry in entries:
            min_value = min_entry.get()
            max_value = max_entry.get()

            if all(i.isdigit() for i in [min_value, max_value]) and int(min_value) < int(max_value):
                self.data[f"{name}_numbers"] = list(range(int(min_value), int(max_value) + 1))
            else:
                min_entry.delete(0, "end")
                max_entry.delete(0, "end")

# Creates a new calculation
    def create_calculation(self):
        operation = random.choice(list(self.data["operations"].keys()))
        if operation == "+":
            x = random.choice(self.data["plus_numbers"])
            y = random.choice(self.data["plus_numbers"])
        elif operation == "-":
            x = random.choice(self.data["minus_numbers"])
            y = random.choice(self.data["minus_numbers"])
        elif operation == "*":
            x = random.choice(self.data["multiply_numbers"])
            y = random.choice(self.data["multiply_numbers"])

        self.data["outcome"] = self.data["operations"][operation](x, y)
        self.math_label.configure(text=f"{x} {operation} {y} = ")

# Triggers when enter is pressed and checks if the answer is correct
    def submit(self, event=None): 
        
        if event and event.char == "\r":
            if "" == self.entry_label.get():
                pass
            elif int(self.data["outcome"]) == int(self.entry_label.get()):
                self.data["score"] += 1
                self.score_label.configure(text=f"Score: {self.data['score']}")
                self.create_calculation()
            else:
                self.data["score"] = 0
                self.score_label.configure(text=f"Score: {self.data['score']}")
                self.create_calculation()
            self.entry_label.delete(0, "end")

# Runs on startup
    def run(self): 
        self.create_calculation()
        self.entry_label.bind("<Return>", self.submit)
        self.app.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()