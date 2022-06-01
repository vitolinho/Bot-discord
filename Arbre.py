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
            if len(self.list_child_node) < 1:
                return False
            if child.keyword in txt :
                child.user_response()

        

    def insert_node(self,Node,Q):
        if self.question == Q:
            self.list_child_node.append(Node)
        elif len(self.list_child_node)>0:
            for N in self.list_child_node:
                N.insert_node(Node,Q)


#first_node = Node("Comment puis-je vous aider ?", "help", [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine ?", "fichier", [])])


node1 = Node("Comment puis-je vous aider ?","help",)

# Choix de l'aide
node1.insert_node(Node("Sur un langage ou un outil ?",["cours","leçon","aide","help","seigneur"],),"Comment puis-je vous aider ?")

# Choix du sujet 
node1.insert_node(Node("Sur un cours particulier (uniquement en python,javascript et php) ou global ?",["langage"]),"Sur un langage ou un outil ?")
node1.insert_node(Node("Sur quel outil ? (figma,photoshop,indesign,git,illustrator)",["outil"],),"Sur un langage ou un outil ?")

# Choix du langage
node1.insert_node(Node("Sur quel langage ? (python,javascript,php,mysql,html,css)",["global"]),"Sur un cours particulier (uniquement en python,javascript et php) ou global ?")
node1.insert_node(Node("Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)",["particulier","précis"]),"Sur un cours particulier (uniquement en python,javascript et php) ou global ?")

# Choix précis sur php, python ou javascript
node1.insert_node(Node("Sur quel langage (python,javascript,php)?",["classes"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")
node1.insert_node(Node("Sur quel langage (php,javascript,python)?",["fonctions"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")
node1.insert_node(Node("Sur quel langage (javascript,python,php)?",["listes"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")
node1.insert_node(Node("Sur quel langage (python,php,javascript)?",["variables"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")
node1.insert_node(Node("Sur quel langage (php,python,javascript)?",["boucles"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")
node1.insert_node(Node("Sur quel langage (javascript,php,python)?",["conditions"]),"Sur quoi ? (variables,fontions,classes,listes,boucle,conditions)")

#  Classes
node1.insert_node(Node("https://docs.python.org/fr/3/tutorial/classes.html",["python"]),"Sur quel langage (python,javascript,php)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes",["javascript"]),"Sur quel langage (python,javascript,php)?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.oop5.php",["php"]),"Sur quel langage (python,javascript,php)?")

# Fonctions
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/09_fonctions/",["python"]),"Sur quel langage (php,javascript,python)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Functions",["javascript"]),"Sur quel langage (php,javascript,python)?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.functions.php",["php"]),"Sur quel langage (php,javascript,python)?")

#  Listes
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/04_listes/",["python"]),"Sur quel langage (javascript,python,php)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array",["javascript"]),"Sur quel langage (javascript,python,php)?")
node1.insert_node(Node("https://www.php.net/manual/fr/function.list.php",["php"]),"Sur quel langage (javascript,python,php)?")

# Variables
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/02_variables/",["python"]),"Sur quel langage (python,php,javascript)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/Variables",["javascript"]),"Sur quel langage (python,php,javascript)?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.variables.php",["php"]),"Sur quel langage (python,php,javascript)?")

# Boucles
node1.insert_node(Node("https://courspython.com/boucles.html",["python"]),"Sur quel langage (php,python,javascript)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Loops_and_iteration",["javascript"]),"Sur quel langage (php,python,javascript)?")
node1.insert_node(Node("https://www.php.net/manual/fr/control-structures.for.php",["php"]),"Sur quel langage (php,python,javascript)?")

# Conditions
node1.insert_node(Node("https://python.doctor/page-apprendre-conditions-structures-conditionnelles-if-else-python-cours-debutant",["python"]),"Sur quel langage (javascript,php,python)?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/if...else",["javascript"]),"Sur quel langage (javascript,php,python)?")
node1.insert_node(Node("https://www.php.net/manual/fr/control-structures.if.php",["php"]),"Sur quel langage (javascript,php,python)?")

# Choix du langage global
node1.insert_node(Node("https://docs.python.org/3/tutorial/index.html",["python"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript",["javascript"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("https://www.php.net/manual/fr/",["php"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("https://sql.sh/",["mysql"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/HTML",["html"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/CSS/Reference",["css"]),"Sur quel langage ? (python,javascript,php,mysql,html,css)")

# Choix de l'outil 
node1.insert_node(Node("https://help.figma.com/hc/en-us",["figma"]),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/fr/photoshop/user-guide.html",["photoshop"]),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/fr/indesign/user-guide.html",["indesign"]),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://helpx.adobe.com/illustrator/user-guide.html",["illustrator"]),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")
node1.insert_node(Node("https://git-scm.com/doc",["git"]),"Sur quel outil ? (figma,photoshop,indesign,git,illustrator)")



#node1.user_response()