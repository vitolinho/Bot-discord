from curses.panel import bottom_panel
from this import d


class Node:

    def __init__(self, question, keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node = []
    
    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()
            if len(self.list_child_node) < 1:
                return False
        

    def insert_node(self,Node,Q):
        if self.question == Q:
            self.list_child_node.append(Node)
        elif len(self.list_child_node)>0:
            for N in self.list_child_node:
                N.insert_node(Node,Q)


    


#first_node = Node("Comment puis-je vous aider ?", "help", [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine ?", "fichier", [])])


node1 = Node("Comment puis-je vous aider ?","help",)

# Choix du support visuel
node1.insert_node(Node("En vidéo ou en article ?","cours",),"Comment puis-je vous aider ?")

# Choix du langage (fr ou en)
node1.insert_node(Node("En français ou en anglais ?","vidéo",),"En vidéo ou en article ?")
node1.insert_node(Node("En français ou en anglais ?","article",),"En vidéo ou en article ?")

# Choix du sujet
node1.insert_node(Node("Sur un langage ou un outil ?","français",),"En français ou en anglais ?")
node1.insert_node(Node("Sur un langage ou un outil ?","anglais",),"En français ou en anglais ?")

node1.insert_node(Node("Sur quel langage ? (python,javascript,php,mysql,html,css)","langage",),"Sur un langage ou un outil ?")
node1.insert_node(Node("Sur quel outil ? (figma,photoshop,indesign,git,illustrator)","outil",),"Sur un langage ou un outil ?")

# Choix du langage de programmation
node1.insert_node(Node("Sur un sujet précis ou global ?","python",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("Sur un sujet précis ou global2 ?","javascript",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("Sur un sujet précis ou global3 ?","php",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("Sur un sujet précis ou global4 ?","mysql",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("Sur un sujet précis ou global5 ?","html",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("Sur un sujet précis ou global6 ?","css",),"Sur quel langage ? (python,javascript,php,mysql,html,css)")

# Choix de l'outil 
node1.insert_node(Node("https://help.figma.com/hc/en-us","figma",),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/fr/photoshop/user-guide.html","photoshop",),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/fr/indesign/user-guide.html","indesign",),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/illustrator/user-guide.html","illustrator"),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://git-scm.com/doc","git",),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")

# Choix des liens globals pour les langages
node1.insert_node(Node("https://docs.python.org/fr/3/","global",),"Sur un sujet précis ou global ?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript","global2",),"Sur un sujet précis ou global2 ?")
node1.insert_node(Node("https://www.php.net/docs.phpL","global3",),"Sur un sujet précis ou global3 ?")
node1.insert_node(Node("https://sql.sh/","global4",),"Sur un sujet précis ou global4 ?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/HTML","global5",),"Sur un sujet précis ou global5 ?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/CSS/Reference","global6",),"Sur un sujet précis ou global6 ?")



node1.user_response()






# $bot : envoie toutes les commandes du bot
# $help : envoie une liste de question posée par le bot à l'utilisateur
# $help_tips : envoie un exemple d'utilisation sur la commande $help
# $admin : envoie un dm à un admin pour répondre au question de l'utilisateur
# $bonus : envoie un lien bonus pour l'utilisateur
# $cours : envoie la liste de cours proposé par le bot
# $tuto : envoie la liste de cours en vidéo proposé par le bot