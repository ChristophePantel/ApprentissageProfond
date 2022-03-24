# ApprentissageProfond
Projet d'Apprentissage Profond à l'ENSEEIHT : Montrer la différence entre des films d'animation 2D, 3D, mélange 2D/3D et Stop Motion

# Utilisation du script screen.py
**Prérequis** : 
    ffmpeg -> https://www.ffmpeg.org/download.html
    magick -> https://imagemagick.org/script/download.php
**Avant utilisation** :
    Il faut absolument faire `chmod +x screen.py` pour rendre le 
    script executable.
**Utilisation** :
    Dans le terminal faire `./screen.py input.txt data_dir` avec
    *data_dir* le directory ou les screens seront enregistres et
    *input.txt* un fichier de la forme :
        nb screen par fichier, categorie, fichier/directory de la/des video a screen
    Il est possible de mettre une entree par ligne.
**Sortie** :
    Les screens sont enregistres dans le directory *data_dir* nommes avec la
    convention *categorie_XXXX.jpg* avec XXXX l'identifiant du screen en 
    fonction de sa categorie. Les images sont deja redimensionnees en 512p.
