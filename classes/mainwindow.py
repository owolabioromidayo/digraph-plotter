import tkinter as tk
from classes.node import Node
from classes.fillnode import FillNode
from classes.node_choice import NodeChoice


"""Creates the main app window"""

class MainWindow:
    def __init__(self, graph_width, height):
        self.nodes = [] # Graph nodes are stored here
        self.graph_width = graph_width
        self.width = self.graph_width + 100 # To make room for button panel
        self.height = height

        self.make_window()
        
        

    def make_window(self):
        """Builds the application window"""

        #Make root
        self.root = tk.Tk() 
        self.root.title("Graph Visualizer")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(width=False, height=False)
        

        #Partition window into button and graph frames
        self.buttons_frame = tk.Frame(self.root, height=self.height, width=100, bg='gray')
        self.buttons_frame.pack(side="left")
        self.buttons_frame.pack_propagate(False)
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side="right")
       
        #Make graph
        self.graph = tk.Canvas(self.graph_frame, width=self.graph_width, height=self.height)
        self.graph.bind('<Button-1>', self.make_node_event) #Binds left click to make_node_event method
        self.graph.pack()

        #Make add button
        # self.loadimage = tk.PhotoImage(file="img/add_button.png")
        # self.add_button = tk.Button(self.buttons_frame, image=self.loadimage, command=self.request_coordinates)
        # self.add_button["border"] = "0"
        # self.add_button.pack(side="top")

        self.root.mainloop()


    def make_node_event(self,event):
        """Creates a node on left mouse click if no node available in area"""
        x = event.x
        y = event.y

        
      
        for node in self.nodes:
            if x  in range(node.x-60,node.x+60) and y in range(node.y-30, node.y+30):
                NodeChoice(self, node)
           

        else:
            self.make_node(x, y)
        


    def make_node(self, x, y):
        """Creates a node given x and y coordinates"""
        if self.nodes == []:
            newnode = Node(x, y, None)
            self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')
        
        else:
            newnode = Node(x, y, self.nodes[-1])
            self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')
            newnode.create_link(self.graph)


        self.nodes.append(newnode)



    # def fillnode(self, node):
    #     """Requests for node coordinates from user"""
    #     FillNode(self, node)