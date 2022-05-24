

class Node:
    def __init__(self,data,Node_right = None,Node_left = None ):
        self.data = data
        self.Node_right = Node_right
        self.Node_left = Node_left
    
    def Add_value(self,data):
        if data == self.data:
            return 
        if data < self.data:
            if self.Node_left == None :
                self.Node_left = Node(data)
            else :
                self.Node_left.Add_value(data)
        else : 
            if self.Node_right == None:
                self.Node_right = Node(data)
            else :
                self.Node_right.Add_value(data)

    def Search(self,value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.Node_left == None:
                return False
            self.Node_left.Search(value)
        else :
            if self.Node_right == None:
                return False
            self.Node_right.Search(value)

    def print_data(self):
        print(self.data)
