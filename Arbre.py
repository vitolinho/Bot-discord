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

node1 = Node("Comment puis-je vous aider ? (**cours**/**leçon**/**aide**)","")

# Choix de l'aide
node1.insert_node(Node("Sur un **langage** ou un **outil** ?",["cours","leçon","aide","seigneur"],),"Comment puis-je vous aider ? (**cours**/**leçon**/**aide**)")

# Choix du sujet 
node1.insert_node(Node("Sur un cours en **particulier** (uniquement en python,javascript et php) ou **global** ?",["langage"]),"Sur un **langage** ou un **outil** ?")
node1.insert_node(Node("Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )",["outil"],),"Sur un **langage** ou un **outil** ?")

# Choix du langage
node1.insert_node(Node("Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )",["global"]),"Sur un cours en **particulier** (uniquement en python,javascript et php) ou **global** ?")
node1.insert_node(Node("Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )",["particulier","précis"]),"Sur un cours en **particulier** (uniquement en python,javascript et php) ou **global** ?")

# Choix précis sur php, python ou javascript
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["classes"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["fonctions"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["listes"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["variables"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["boucles"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")
node1.insert_node(Node("Sur quel langage ( **Python** , **JavaScript** , **PHP** )?",["conditions"]),"Sur quoi ? ( **variables** , **fontions** , **classes** , **listes** , **boucles** , **conditions** )")

#  Classes
node1.insert_node(Node("https://docs.python.org/fr/3/tutorial/classes.html",["python","Python"]),"Sur quel langage  **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes",["javascript","JavaScript"]),"Sur quel langage  **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.oop5.php",["php","PHP"]),"Sur quel langage  **Python** , **JavaScript** , **PHP** )?")

# Fonctions
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/09_fonctions/",["python","Python"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Functions",["javascript","JavaScript"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.functions.php",["php","PHP"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")

#  Listes
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/04_listes/",["python","Python"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array",["javascript","JavaScript"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/function.list.php",["php","PHP"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")

# Variables
node1.insert_node(Node("https://python.sdv.univ-paris-diderot.fr/02_variables/",["python","Python"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/Variables",["javascript","JavaScript"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/language.variables.php",["php","PHP"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")

# Boucles
node1.insert_node(Node("https://courspython.com/boucles.html",["python","Python"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Loops_and_iteration",["javascript","JavaScript"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/control-structures.for.php",["php","PHP"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")

# Conditions
node1.insert_node(Node("https://python.doctor/page-apprendre-conditions-structures-conditionnelles-if-else-python-cours-debutant",["python","Python"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/if...else",["javascript","JavaScript"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")
node1.insert_node(Node("https://www.php.net/manual/fr/control-structures.if.php",["php","PHP"]),"Sur quel langage ( **Python** , **JavaScript** , **PHP** )?")

# Choix du langage global
node1.insert_node(Node("https://docs.python.org/3/tutorial/index.html",["python","Python"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/JavaScript",["javascript","JavaScript"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")
node1.insert_node(Node("https://www.php.net/manual/fr/",["php","PHP"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")
node1.insert_node(Node("https://sql.sh/",["mysql","MySQL"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/HTML",["html","HTML"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")
node1.insert_node(Node("https://developer.mozilla.org/fr/docs/Web/CSS/Reference",["css","CSS"]),"Sur quel langage ? ( **Python** , **JavaScript** , **PHP** , **MySQL** , **HTML** , **CSS** )")

# Choix de l'outil 
node1.insert_node(Node("https://help.figma.com/hc/en-us",["figma","Figma"]),"Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )")
node1.insert_node(Node("https://helpx.adobe.com/fr/photoshop/user-guide.html",["photoshop","Photoshop"]),"Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )")
node1.insert_node(Node("https://helpx.adobe.com/fr/indesign/user-guide.html",["indesign","Indesign"]),"Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )")
node1.insert_node(Node("https://helpx.adobe.com/illustrator/user-guide.html",["illustrator","Illustrator"]),"Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )")
node1.insert_node(Node("https://git-scm.com/doc",["git","Git"]),"Sur quel outil ? ( **Figma** , **Photoshop** , **Indesign** , **Git** , **Illustrator** )")