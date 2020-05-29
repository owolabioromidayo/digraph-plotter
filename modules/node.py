import tkinter as tk


class Node:
    def __init__(self, x, y, prevnode=None, message=None):
        self.x = x
        self.y = y
        self.prevnode = prevnode
        self.message = message

    def create_link(self, graph):
        """Links nodes"""

        # if prevnode and currnode are on relatively the same y levels
        if abs(self.prevnode.y - self.y) <= 100:

            # if prevnode is to the left curr node: currnode snap point at left and prevnode snap point at right
            if self.prevnode.x < self.x:
                graph.create_line(
                    self.x-50, self.y, self.prevnode.x+50, self.prevnode.y, arrow=tk.FIRST
                )

            # prevnode to the right: currnode snap point at the right and prevnode snap point at left
            else:
                graph.create_line(
                    self.x+50, self.y, self.prevnode.x-50, self.prevnode.y, arrow=tk.FIRST
                )

        # if prevnode above currnode : create link to bottom  of prevnode from top  of curr node
        elif self.y < self.prevnode.y:

            graph.create_line(
                self.x, self.y+20, self.prevnode.x, self.prevnode.y-20, arrow=tk.FIRST
            )

        # currnode above prevnode : link from bottom of currnode to top of prevnode
        elif self.y > self.prevnode.y:
            graph.create_line(
                self.x, self.y-20, self.prevnode.x, self.prevnode.y+20, arrow=tk.FIRST
            )

        else:
            pass
