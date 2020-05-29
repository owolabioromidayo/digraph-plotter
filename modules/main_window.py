import random, json, os, sys, threading
import tkinter as tk
from tkinter import filedialog, messagebox
from modules.node import Node
from modules.node_choice import NodeChoice





"""Creates the main app window, also contains some node helper functions"""


class MainWindow:
    def __init__(self, graph_width, height):
        self.nodes = []  # Graph nodes are stored here
        self.graph_width = graph_width
        self.width = self.graph_width + 100  # To make room for button panel
        self.height = height

        self.exec_new_thread(self.make_window)

        # self.make_window()


    
    def exec_new_thread(self, proc):
        new_thread = threading.Thread(target=proc)
        new_thread.start()
        new_thread.join()
        
        

    def make_window(self):
        """Builds the application window"""

        # Make root
        self.root = tk.Tk()
        self.root.title("Graph Visualizer")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(width=False, height=False)
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Partition window into button and graph frames
        self.buttons_frame = tk.Frame(
            self.root, height=self.height, width=100, bg='gray'
        )
        self.buttons_frame.pack(side="left")
        self.buttons_frame.pack_propagate(False)

        self.save_button  = tk.Button(self.buttons_frame, text='Save state', command=self.save_state)
        self.save_button.pack()


        self.load_state_btn  = tk.Button(self.buttons_frame, text='Load state', command=self.load_state)
        self.load_state_btn.pack()

        self.new_win_btn  = tk.Button(self.buttons_frame, text='New Window', command=self.new_window)
        self.new_win_btn.pack()


        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side="right")

        # Make graph
        self.graph = tk.Canvas(
            self.graph_frame, width=self.graph_width, height=self.height
        )
        # Binds left click to make_node_event method
        self.graph.bind('<Button-1>', self.make_node_event)
        self.graph.pack()

        self.root.mainloop()

    def make_node(self, x, y, message=None, prevnode=None):
        """Creates a node given x and y coordinates"""

        # border blocking- all created nodes must be fully shown on screen : create a border of 50 around the graph space
        if x < 50 or x > self.width-150:
            return

        if y < 50 or y > self.height-50:
            return

        # for first node
        if self.nodes == []:
            newnode = Node(x, y, prevnode)
            self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')

        # for other nodes
        else:
            newnode = Node(x, y, self.nodes[-1])
            self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')
            newnode.create_link(self.graph)

        self.nodes.append(newnode)
        return newnode

    def make_node_event(self, event):
        """make_node event handler"""
        x = event.x
        y = event.y

        for node in self.nodes:  # Finds a node in range to attach to
            if x in range(node.x-60, node.x+60) and y in range(node.y-30, node.y+30):
                NodeChoice(self, node)

        else:
            self.make_node(x, y)


    def save_state(self):
        #collect objects & save in json format
        #object unpacker to load state using file dialog

        save_info =  {}
        for idx, node in enumerate(self.nodes):
            save_info[idx] = [node.x, node.y, self.nodes.index(node.prevnode) if node.prevnode is not None else None, node.message]
            

        # save_info = [(x,y,prevnode,message) for x,y,prevnode,message in (node.x,node.y,node.prevnode,node.message) for node in self.nodes]
        filename = filedialog.asksaveasfilename(defaultextension="txt", initialdir=os.getcwd())
        with open(filename, 'w') as f:
            json_string = json.dumps(save_info)
            json.dump(json_string,f)


    
    def load_state(self):

        filename = filedialog.askopenfilename(initialdir=os.getcwd())
        with open(filename) as f:
            json_string = json.load(f)
            load_info = json.loads(json_string)
            print(load_info[str(0)])

        for idx, node in load_info.items():
            x, y, prev, msg = node
            if prev is not None :
                assert int(idx) > prev 
                prev = self.nodes[prev]
            
            self.load_node(x, y, prev, msg)




    def load_node(self, x, y, prevnode=None, message=None):
        """Load nodes from dict"""

        # border blocking- all created nodes must be fully shown on screen : create a border of 50 around the graph space
        # if x < 50 or x > self.width-150:
        #     return

        # if y < 50 or y > self.height-50:
        #     return

        # for first node
        # if self.nodes == []:
        #     newnode = Node(x, y, prevnode)
        #     self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')

        # # for other nodes
        # else:
        #     newnode = Node(x, y, self.nodes[-1])
        #     self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')
        #     newnode.create_link(self.graph)


        newnode = Node(x,y, prevnode, message)
        self.graph.create_rectangle(x-50, y-20, x+50, y+20, fill='red')
        if prevnode is not None : newnode.create_link(self.graph) 
        if message is not None : self.graph.create_text((x,y), text=message) 

        self.nodes.append(newnode)
        return newnode



    def new_window(self):
        self.exec_new_thread(self.make_window)


    def on_closing(self):
         if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()




    def make_random_node(self):
        x, y = random.randint(0, self.width), random.randint(0, self.height)
        self.make_node(x, y)

    # def _test_space(self):
    #     """Generate node relationships from adjacency matrix"""
    #     pass
    #     adj_mat = [[0, 'a', 'b', 'c', 'd'],
    #                ['a', 0, 1, 0, 1],
    #                ['b', 1, 0, 0, 0],
    #                ['c', 0, 0, 0, 1],
    #                ['d', 1, 0, 1, 0]]

    #     nodes = []
    #     for n in adj_mat[0][1:]:
    #         print(n)
    #         x, y = random.randint(
    #             0, self.width-150), random.randint(0, self.height-50)
    #         node = self.make_node(x, y)
    #         node.message = str(n)
    #         self.graph.create_text((node.x, node.y), text=node.message)
    #         nodes.append(node)
