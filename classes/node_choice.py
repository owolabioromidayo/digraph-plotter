import tkinter as tk
from classes.fillnode import FillNode

class NodeChoice:
    def __init__(self, parent, node):
        self.parent = parent #this is an instance of the MainWindow class
        self.node = node

        #Make window
        self.root = tk.Tk()
        self.root.title('Current Node Options')
        self.root.bind('<Return>', self.on_enter) 
        self.label = tk.Label(self.root, text="Make a Choice")
        self.label.grid(row=0,column=0, pady=10, padx=10)

        

        self.choice = tk.IntVar(self.root)
    

        self.rbtn1 = tk.Radiobutton(self.root, text="Link", variable=self.choice, value=0)
        self.rbtn1.grid(row=1,column=0)


        self.rbtn2 = tk.Radiobutton(self.root, text="Rename", variable=self.choice, value=1)
        self.rbtn2.grid(row=2, column=0)

        
        self.button = tk.Button(self.root, text='Confirm',command=self.on_button_press)
        self.button.grid(row=3,column=0,pady=10)
        self.root.mainloop()


    def on_button_press(self):
        self.choice = self.choice.get()
        self.root.destroy()

        if self.choice == 1:
            FillNode(self.parent, self.node)

        else:
            #on choice makenode
            self.parent.nodes.remove(self.node)
            self.parent.nodes.append(self.node)

    def on_enter(self, event):
        self.on_button_press()
        

