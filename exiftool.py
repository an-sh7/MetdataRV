import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Get the directory path where the current Python script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Assign the path of exiftool.exe
tool_path = os.path.join(script_dir, "exiftool.exe")

# Function to read metadata
def read_metadata():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        output_text.delete(1.0, tk.END)  # Clear the output text area
        read_data = subprocess.run([tool_path, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, read_data.stdout)
        output_text.insert(tk.END, read_data.stderr)

# Function to remove all metadata
def remove_all_metadata():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        output_text.delete(1.0, tk.END)  # Clear the output text area
        delete_data = subprocess.run([tool_path, "-all=", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, delete_data.stdout)
        output_text.insert(tk.END, delete_data.stderr)

# GUI
root = tk.Tk()
root.title("Metadata Remover and Viewer")

# Making it DarkMode
bg_color = "#333333"  
fg_color = "#FFFFFF"  
button_bg_color = "#444444"  
button_fg_color = "#FFFFFF"  

root.configure(bg=bg_color)

#Button to Read Data
read_button = tk.Button(root, text="Read Metadata", command=read_metadata, bg=button_bg_color, fg=button_fg_color)
read_button.pack(pady=5)

#Button the Remove Data
remove_button = tk.Button(root, text="Remove All Metadata", command=remove_all_metadata, bg=button_bg_color, fg=button_fg_color)
remove_button.pack(pady=5)

#Output Box
output_text = tk.Text(root, height=20, width=100, bg=bg_color, fg=fg_color) 
output_text.pack(pady=10)

root.mainloop()