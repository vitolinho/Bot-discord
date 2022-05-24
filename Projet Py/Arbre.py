class Node:

    def __init__(self, question, keyword, list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node
    
    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()

first_node = Node("Comment puis-je vous aider ?", "help", [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine ?", "fichier", [])])

Node.user_response(first_node)