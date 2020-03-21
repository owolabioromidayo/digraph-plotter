import tkinter as tk
from classes.promptwindow import PromptWindow
        

class FillNode(PromptWindow):
    """Requests for node coordinates from the user"""

    def __init__(self, parent, node):
        self.node = node
        super().__init__(parent, message="Enter node info")
       

    def on_button_press(self):
        """Parse Inputed Coordinates and Makes Nodes of Valid Ones"""

        # if self.node == None:
        #     self.node = self.parent.nodes[-1]

        self.node.message = self.entry.get()
        self.parent.graph.create_text((self.node.x, self.node.y), text=self.node.message)
        self.root.destroy()