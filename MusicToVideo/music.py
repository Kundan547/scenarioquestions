import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from tkinter import messagebox

# Creating main window
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and resizing property
root.title("First - Video to Audio Converter")
root.geometry("600x310")
root.resizable(width=False, height=False)
root.configure(background="#3b4370")

# function to browse input file
def browse_input_command():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("mp3 files", "*.mp4"), ("all files", "*.*")))
  
    # display file path in label
    input_file_path_label.config(text=file_path)

# function to browse output file
def browse_output_command():
    global output_path
    output_path = filedialog.asksaveasfilename(initialdir="/", title="Save file as", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
  
    # display file path in label
    output_file_path_label.config(text=output_path)

# function to convert video to audio
def convert_command():
    global file_path
    global output_path
    video = AudioSegment.from_file(file_path)
    video.export(output_path, format="mp3")
    messagebox.showinfo("Success", "Video converted to Audio successfully")

# Create a label to display the title
title_label=tk.Label(root)
title_label.configure(background="#90f090", foreground="#333333", font="Arial 18 bold", justify="center", text="TechVidvan - Video to Audio Converter")
title_label.place(x=0,y=0,width=600,height=50)

# Create a button to browse input file
browse_input_button=tk.Button(root)
browse_input_button.configure(font="Arial 14", justify="center", text="Browse Input", command=browse_input_command)
browse_input_button.place(x=30,y=80,width=160,height=40)

# Create a label to display file path
input_file_path_label=tk.Label(root)
input_file_path_label.configure(background="#3b4370", foreground="#ffffc5", font="Arial 14", justify="center", text="File Path")
input_file_path_label.place(x=220,y=80,width=360,height=40)

# Create a button to browse output file
browse_output_button=tk.Button(root)
browse_output_button.configure(font="Arial 14", justify="center", text="Output Path ", command=browse_output_command)
browse_output_button.place(x=30,y=150,width=160,height=40)

# Create a label to display file path
output_file_path_label=tk.Label(root)
output_file_path_label.configure(background="#3b4370", foreground="#ffffc5", font="Arial 14", justify="center", text="File Path")
output_file_path_label.place(x=220,y=150,width=360,height=40)

# Create a button to convert video to audio
convert_button=tk.Button(root)
convert_button.configure(font="Arial 14", justify="center", text="Convert", command=convert_command)
convert_button.place(x=220,y=240,width=160,height=40)

# Run the main window loop
root.mainloop()