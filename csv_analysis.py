import os # importe la laibrairie OS. Permet d'utiliser des fonctionnalités qui dépendent du système d'exploitation. Comme lire et écrire dans un fichier. 

def launch_analysis(data_file): # définition d'une fonction launch_analysis
    directory = os.path.dirname(__file__) # la variable directory va contenir le bon chemin vers notre fichier grâce à la variable __file__
    path_to_file = os.path.join(directory, "data", data_file) # la variable path_to_file se rend dans le dossier "data" et y sélectionne le fichier (data_file) qui correspond à la variable directory

    with open(path_to_file, "r") as f: # ouvre le fichier contenu dans la variable path_to_file et lui attribue la variable f
        preview = f.readline() # la variable preview lit la première ligne du fichier f

    print("Yeah! We managed to read the file. Here is a preview : {}".format(preview)) # affiche la variable preview

if __name__ == "__main__":
    launch_analysis('current_mps.csv') # lance la fonction launch_analysis si le fichier est lu comme script principal