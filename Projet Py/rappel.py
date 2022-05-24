### Les Listes

## stockage de données avec un Liste
A = [1,2,3,4,5]
## parcourir une liste
# méthode 1
for val in A:
    print(val)

# méthode 2

for i in range(len(A)):
    print(A[i])

## stockage de données avec un dictionnaire
Dict = {
    "nom" : { "nom1" : "Vitomir",
            "nom2" : "Victor"
    },
    "age" : 19,
}
### Les dictionnaires

## Afficher les données du dictionnaire
print(Dict["nom"])
print(Dict["age"])

# afficher les clés
for key in Dict.keys():
    print(key)

# afficher les valeurs dans les clés
for key in Dict.keys():
    print(Dict[key])

# afficher les valeurs
for value in Dict.values():
    print(value)

# afficher les deux
for key, value in Dict.items():
    print(key, value)