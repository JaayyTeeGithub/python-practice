from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()
print(filename)
subject = input("Enter subject of message: ")
message = "Subject: " + subject + "\n \n"

with open(filename) as file_object:
    for line in file_object:
        message = message + line

print(message)
