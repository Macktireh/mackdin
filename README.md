# Mackdin

## Introduction

Mackdin c'est un projet réseau social (clone Linkedin) que j'ai réalisé pour me donner un petit challenge en rentrant du travail le soir et quelques week-ends. Mackdin est construit en Python avec Django et un peu de React js.

Pour toute proposition ou contribution est la bienvenue.

Lien du site : <https://mackdin.herokuapp.com/>

![](static/home/img/mackdin.jpg)

**Les technologies utilisés :** 

* Python
* Django
* PostgreSQL
* JavaScript
* React
* HTML
* SASS
* Heroku
* Gunicorn
* Cloudinary

## Installation

### 1. Pré-requis

Vous devez avoir sur votre machine Python, NodeJS et Git installer.

### 2. Récuperer le projet

Ouvrer un terminal et exécuter les commandes suivantes:

```bash
git clone https://github.com/Macktireh/mackdin.git
cd mackdin
```

### 3. Créer et activer un environnement virtual

Créer l'environnement virtual:
```bash
python -m venv .venv
```

Activer l'environnement virtual:

***Pour Windows :***

```bash
.venv\Scripts\activate.bat
```

***Pour Linux et Mac os :***

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```
### 5. Configurer les variables d'environnement

Renommer le fichier .env.example en .env et renseigner vos informations personnelles. 
Puis executer les migrations :

```bash
python manage.py migrate
```

Ensuite lancer le server de développement :

```bash
python manage.py runserver
```
