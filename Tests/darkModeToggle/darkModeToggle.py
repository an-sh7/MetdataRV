import tkinter as tk

def toggle_mode():
    global dark_mode
    if dark_mode:
        set_normal_mode()
    else:
        set_dark_mode()
    dark_mode = not dark_mode

def set_dark_mode():
    root.config(bg=bg_dark)
    toggle_button.config(bg=highlight_dark, fg=fg_dark, activebackground=select_dark, activeforeground=fg_dark)

def set_normal_mode():
    root.config(bg=bg_normal)
    
    toggle_button.config(bg=highlight_normal, fg=fg_normal, activebackground=select_normal, activeforeground=fg_normal)

root = tk.Tk()
root.title("Toggle Dark Mode Example")

# Define dark mode colors
bg_dark = "#2e2e2e"
fg_dark = "#ffffff"
select_dark = "#3e3e3e"
highlight_dark = "#4e4e4e"

# Define normal mode colors
bg_normal = "#f0f0f0"
fg_normal = "#000000"
select_normal = "#d3d3d3"
highlight_normal = "#c0c0c0"

# Initial mode
dark_mode = False


# Creating Toggle Button for switching modes
toggle_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_mode, font=("Arial", 12))

# Setting the initial mode
set_normal_mode()

toggle_button.pack(padx=20, pady=10)

root.mainloop()
