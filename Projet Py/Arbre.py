from curses.panel import bottom_panel


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
    
   #def insert_node(self,Node,question):


first_node = Node("Comment puis-je vous aider ?", "help", [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine ?", "fichier", [])])

Node.user_response(first_node)

# $bot : envoie toutes les commandes du bot
# $help : envoie une liste de question posée par le bot à l'utilisateur
# $help_tips : envoie un exemple d'utilisation sur la commande $help
# $admin : envoie un dm à un admin pour répondre au question de l'utilisateur
# $bonus : envoie un lien bonus pour l'utilisateur
# $cours : envoie la liste de cours proposé par le bot
# $tuto : envoie la liste de cours en vidéo proposé par le bot