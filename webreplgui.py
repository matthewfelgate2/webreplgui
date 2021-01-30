import webrepl
import tkinter as tk
from tkinter import IntVar
import os

# Run button 
def run():
    myCommand =  "webreplcmd --host "  + address.get()

    #Port
    if (len(str(port.get())) != 0):
        myCommand +=  " --port " + port.get()

    #Debug
    if (debugVar.get() == 1):
        myCommand += " --debug "

    #Verbose
    if (verboseVar.get() == 1):
        myCommand += " --verbose "

    #Password
    if (len(str(password.get())) != 0):
        myCommand += " --password " + password.get() 

    #Command
    if (len(str(cmd.get())) != 0):
        myCommand += " " + cmd.get() 

    # Run command in command line and get returned text
    stream = os.popen(myCommand)
    output = stream.read()

    # If no output then put a done message to tell user finished. 
    if(len(output)==0):
        output='Done.'

    # Write output to the box
    command.configure(text=output)


# Root
root = tk.Tk()
root.geometry("500x700")
root.title('GUI for Web Repl')

# Intro text
msg = tk.Message(root, text ="A simple graphical interface for Web REPL", width=1900)
msg.pack()

# Ip Address
addressLabel = tk.Label(root, text="IP address (required)")
addressLabel.pack()
address = tk.Entry(root)
address.insert(0, '192.168.0.128')
address.pack()

# Port number
portLabel = tk.Label(root, text="Port number (optional)")
portLabel.pack()
port = tk.Entry(root)
port.insert(0, "8266")
port.pack()

#Password
passwordLabel = tk.Label(root, text="Password (optional)")
passwordLabel.pack()
password = tk.Entry(root)
password.insert(0, "password")
password.pack()

# Command to run 
cmdLabel = tk.Label(root, text="Command (optional)")
cmdLabel.pack()
cmd = tk.Entry(root)
cmd.insert(0, 'ls')
cmd.pack()

# Debug Checkbox
debugVar = IntVar()
debug = tk.Checkbutton(root, text="Debug", variable=debugVar, onvalue=1, offvalue=0)
debug.pack()

# Verbose Checkbox
verboseVar = IntVar()
verbose = tk.Checkbutton(root, text="Verbose", variable=verboseVar, onvalue=1, offvalue=0)
verbose.pack()

# Command Text
commandLabel = tk.Message(root, text="Output:")
commandLabel.pack()
command = tk.Message(root, text="...", fg='red')
command.pack()

# Run Buttom
run = tk.Button(root, text="Run", command=run)
run.pack()

# End by running loop
tk.mainloop()