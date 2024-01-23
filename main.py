import customtkinter
import random
#------------------------------x
app = customtkinter.CTk()
app.geometry("400x300")
app.title("Mental Math Practice")

frame = customtkinter.CTkFrame(app, corner_radius=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

title_label = customtkinter.CTkLabel(frame, text="Mental Math Practice")
title_label.grid(row=0, column=0,columnspan=4, padx=40, pady=20)

dummy_label = customtkinter.CTkLabel(frame, text="")
dummy_label.grid(row=1, column=0, padx=20)

dummy_label1 = customtkinter.CTkLabel(frame, text="")
dummy_label1.grid(row=1, column=3, padx=20)

math_label = customtkinter.CTkLabel(frame, text="0 + 0 = ")
math_label.grid(row=1, column=1, padx=0, pady=20)

entry_label = customtkinter.CTkEntry(frame, placeholder_text="")
entry_label.grid(row=1, column=2, padx=0, pady=20)

score_label = customtkinter.CTkLabel(frame, text="Score: 0", text_color="gray")
score_label.grid(row=2, column=0,columnspan=4, padx=40, pady=20)
#--------------------------------x
score = 0
numbers = list(range(1, 101))
operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
outcome = 0

def create_calculation():
    global outcome
    x = random.choice(numbers)
    y = random.choice(numbers)

    operation = random.choice(list(operations.keys()))
    outcome = operations[operation](x, y)

    math_label.configure(text=f"{x} {operation} {y} = ")

def submit(event=None):
    global outcome, score
    if event and event.char == '\r':
        if '' == entry_label.get():
            pass
        elif int(outcome) == int(entry_label.get()):
            score += 1
            score_label.configure(text=f"Score: {score}")
            create_calculation()
        else:
            score = 0
            score_label.configure(text=f"Score: {score}")
            create_calculation()
        entry_label.delete(0, 'end')

if __name__ == "__main__":
    entry_label.bind("<Return>", submit)
    create_calculation()
    app.mainloop()
