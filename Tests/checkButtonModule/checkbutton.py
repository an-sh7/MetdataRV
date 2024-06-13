import tkinter as tk

def on_button_toggle():
    if var.get() == 1:
        checkbutton.config(text="Feature Enabled")
    else:
        checkbutton.config(text="Enable Feature")

root = tk.Tk()

# Creating a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var, 
                             onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Placing the Checkbutton in the window
checkbutton.pack(padx=40, pady=40)

root.mainloop()
