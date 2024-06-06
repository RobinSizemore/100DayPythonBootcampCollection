import tkinter


window = tkinter.Tk()
window.config(padx=20, pady=20)
window.columnconfigure(0, uniform="1")
window.columnconfigure(1, uniform="1")
window.columnconfigure(2, uniform="1")

miles_entry = tkinter.Entry()
miles_entry.config(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Noto Sans", 10, "bold"), anchor="w")
miles_label.grid(column=2, row=0, sticky="w")

explanation_label = tkinter.Label(text="is equal to 0 Km")
explanation_label.grid(column=0, row=1, columnspan=3)


def convert_mi_to_km():
    miles = miles_entry.get()
    kilometers = float(miles) * 1.61
    explanation_label["text"] = f"is equal to {round(kilometers, 3)} Km."


calculate_button = tkinter.Button(text="Calculate", command=convert_mi_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
