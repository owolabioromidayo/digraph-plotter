import tkinter as tk
from classes.fillnode import FillNode

class NodeChoice:
    def __init__(self, parent, node):
        self.parent = parent #this is an instance of the MainWindow class
        self.node = node

        #Make window
        self.root = tk.Tk()
        self.root.title('')
        self.label = tk.Label(self.root, text="Make a Choice")
        self.label.grid(row=0,column=0)

        

        self.choice = tk.StringVar(self.root)
        self.choice.set("link") # default value

        self.options = tk.OptionMenu(self.root, self.choice, "link", "rename")
        self.options.grid(row=1,column=0, padx=0, pady=5)

        self.options.bind('<Return>', self.on_enter) 
        self.button = tk.Button(self.root, text='Confirm',command=self.on_button_press)
        self.button.grid(row=2,column=0,pady=10)
        self.root.mainloop()


    def on_button_press(self):
        self.choice = self.choice.get()
        self.root.destroy()

        if self.choice == "rename":
            FillNode(self.parent, self.node)

        else:
            #on choice makenode
            self.parent.nodes.remove(self.node)
            self.parent.nodes.append(self.node)

    def on_enter(self, event):
        self.on_button_press()
        

