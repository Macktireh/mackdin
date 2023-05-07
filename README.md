# Mackdin

## Introduction

Mackdin est un projet réseau social (clone LinkedIn personnalisé), j'ai réalisé en Python avec Django et un peu de React.

  <!-- <table>
    <tr>
      <td>
        <img src="static/home/img/mackdin_1.png" width=400 />
      </td>
      <td>
        <img src="static/home/img/mackdin_2.png" width=400 />
      </td>      
    </tr>   
    <tr>
      <td>
        <img src="static/home/img/mackdin_3.png" height=400 />
      </td>
      <td>
        <img src="static/home/img/mackdin_4.png" height=400 />
      </td>      
    </tr>   
</table> -->

 
<img src="static/home/img/mackdin_1.png" width=500 />
<img src="static/home/img/mackdin_2.png" width=500 />
<img src="static/home/img/mackdin_3.png" width=400 />
<img src="static/home/img/mackdin_4.png" width=400 />

<!--
![](static/home/img/mackdin_1.png)
![](static/home/img/mackdin_2.png)
![](static/home/img/mackdin_3.png)
![](static/home/img/mackdin_4.png)
![](static/home/img/mackdin_5.png) -->

**Les technologies utilisés :**

- Python
- Django
- PostgreSQL
- JavaScript
- React
- SASS
- Cloudinary

## Installation

### 1. Pré-requis

Python 3.7+, NodeJS et Git.

### 2. Cloner le projet

Ouvrer un terminal et exécuter les commandes suivantes:

```bash
git clone https://github.com/Macktireh/mackdin.git
cd mackdin
```

### 3. Créer et activer l'environnement virtual

Créer l'environnement virtual:

```bash
python -m venv .venv
```

Activer l'environnement virtual:

**_Pour Windows :_**

```bash
.venv\Scripts\activate.bat
```

**_Pour Linux et Mac os :_**

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Configurer les variables d'environnement

Renommer le fichier .env.example en .env et renseigner vos informations personnelles.
Puis appliquer les migrations :

```bash
python manage.py migrate
```

Ensuite lancer le server de développement :

```bash
python manage.py runserver
```

Aller sur http://127.0.0.1:8000 dans un navigateur web.
