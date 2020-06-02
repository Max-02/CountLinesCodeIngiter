import os

#Ordner
folder = [
    "Controllers",
    "Models",
    "Views"
]

#Ordner, die nicht gezählt werden sollen
blacklist_folder = [
    'Views/errors',
]

#Datein, die nicht gezählt werden sollen
blacklist_file = [
    'Views/welcome_message.php'
]

fileending = ".php"

def countLinesOfFolder(folderpath, spaces):

    #Falls Order in Blacklist
    if folderpath in blacklist_folder:
        return 0

    print(spaces + folderpath)

    #Holt Inhalt aus Ordner
    files = os.listdir(folderpath)

    #Zählt die Zeilen
    folderlines = 0

    #Geht über die Files
    for filename in files:
        #Pfad der Datei
        path = folderpath + "/" + filename
        #Wenn php File dann Zeilen zählen
        if fileending in filename and path not in blacklist_file : 
            num_lines = sum(1 for line in open(path))
            print(spaces + "  " +  path + ": " + str(num_lines))
            folderlines += num_lines
        #Wenn Order dann die Funktion wieder aufrufen 
        elif "." not in filename:
            folderlines += countLinesOfFolder(folderpath + "/" + filename, spaces + "  ")
    return folderlines

lines = 0
print("------------------------------------")
#Geht durch die Ordner
for foldername in folder:

    #Zeilen des jeweiligen Ordners zählen
    folderlines = countLinesOfFolder(foldername, "")   
    lines += folderlines

    #Zeilen des einzelnen Ordners ausgeben
    print("------------------------------------")
    print(foldername + ": " + str(folderlines))
    print("------------------------------------")

#Gesamtzahl ausgeben
print("Overall: " + str(lines))