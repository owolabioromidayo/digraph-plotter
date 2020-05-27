import tkinter as tk
from modules.node import Node
from modules.node_choice import NodeChoice
import random


"""Creates the main app window, also contains some node helper functions"""


class MainWindow:
    def __init__(self, graph_width, height):
        self.nodes = []  # Graph nodes are stored here
        self.graph_width = graph_width
        self.width = self.graph_width + 100  # To make room for button panel
        self.height = height

        self.make_window()

    def make_window(self):
        """Builds the application window"""

        # Make root
        self.root = tk.Tk()
        self.root.title("Graph Visualizer")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(width=False, height=False)

        # Partition window into button and graph frames
        self.buttons_frame = tk.Frame(
            self.root, height=self.height, width=100, bg='gray'
        )
        self.buttons_frame.pack(side="left")
        self.buttons_frame.pack_propagate(False)
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

    def make_node(self, x, y):
        """Creates a node given x and y coordinates"""

        # border blocking- all created nodes must be fully shown on screen : create a border of 50 around the graph space
        if x < 50 or x > self.width-150:
            return

        if y < 50 or y > self.height-50:
            return

        # for first node
        if self.nodes == []:
            newnode = Node(x, y, None)
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

    def make_random_node(self):
        x, y = random.randint(0, self.width), random.randint(0, self.height)
        self.make_node(x, y)

    def _test_space(self):
        """Generate node relationships from adjacency matrix"""
        pass
        adj_mat = [[0, 'a', 'b', 'c', 'd'],
                   ['a', 0, 1, 0, 1],
                   ['b', 1, 0, 0, 0],
                   ['c', 0, 0, 0, 1],
                   ['d', 1, 0, 1, 0]]

        nodes = []
        for n in adj_mat[0][1:]:
            print(n)
            x, y = random.randint(
                0, self.width-150), random.randint(0, self.height-50)
            node = self.make_node(x, y)
            node.message = str(n)
            self.graph.create_text((node.x, node.y), text=node.message)
            nodes.append(node)
