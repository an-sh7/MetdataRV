import tkinter as tk

def execute_command():
    if var1.get() == 1:
        print("Checkbutton 1 is selected")
    else:
        print("Checkbutton 1 is deselected")

    if var2.get() == 1:
        print("Checkbutton 2 is selected")
    else:
        print("Checkbutton 2 is deselected")

def on_button_toggle1():
    if var1.get() == 1:
        checkbutton1.config(text="Feature 1 Enabled")
    else:
        checkbutton1.config(text="Enable Feature 1")

def on_button_toggle2():
    if var2.get() == 1:
        checkbutton2.config(text="Feature 2 Enabled")
    else:
        checkbutton2.config(text="Enable Feature 2")

root = tk.Tk()

# Creating Checkbutton 1
var1 = tk.IntVar()
checkbutton1 = tk.Checkbutton(root, text="Enable Feature 1", variable=var1, 
                              onvalue=1, offvalue=0, command=on_button_toggle1)

# Creating Checkbutton 2
var2 = tk.IntVar()
checkbutton2 = tk.Checkbutton(root, text="Enable Feature 2", variable=var2, 
                              onvalue=1, offvalue=0, command=on_button_toggle2)

# Setting options for Checkbutton 1
checkbutton1.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                    selectcolor="green", relief="raised", padx=10, pady=5)

# Setting options for Checkbutton 2
checkbutton2.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                    selectcolor="green", relief="raised", padx=10, pady=5)

# Creating Execute Button
execute_button = tk.Button(root, text="Execute", command=execute_command)

# Placing the Checkbuttons and Execute button in the window
checkbutton1.pack(padx=20, pady=20)
checkbutton2.pack(padx=20, pady=20)
execute_button.pack(padx=20, pady=20)

root.mainloop()
