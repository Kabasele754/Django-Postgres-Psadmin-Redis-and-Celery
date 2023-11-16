# Django-Postgres-Psadmin-Redis-and-Celery

Ce projet est une application web basée sur Django, utilisant Docker pour la gestion des conteneurs, PostgreSQL comme base de données, psadmin pour l'administration du serveur, Celery pour la gestion des tâches asynchrones et Redis comme broker de message.

## Part#1
### Créer une image à partir du Dockerfile dans le répertoire actuel avec le tag python-django
```docker build --tag python-django .```

### Lancer un conteneur à partir de l'image créée précédemment et publier le port 8000
```docker run --publish 8000:8000 python-django```

## Part#2
### Construire les services spécifiés dans le fichier docker-compose.yml
```docker-compose build```

### Exécuter une commande dans un nouveau conteneur app en utilisant django-admin pour démarrer un projet nommé parameter

```docker-compose run --rm app django-admin startproject parameter .
```
### Démarrer les services spécifiés dans le fichier docker-compose.yml

```docker-compose up```


## Part#3
### Construire les services spécifiés dans le fichier docker-compose.yml
```docker-compose build```

### Exécuter une commande dans un nouveau conteneur app en utilisant django-admin pour démarrer un projet nommé parameter
```docker-compose run --rm app django-admin startproject parameter .```

### Démarrer les services spécifiés dans le fichier docker-compose.yml
```docker-compose up```

### Exécuter une commande dans le conteneur django_app pour ouvrir un shell interactif
```docker exec -it django_app /bin/bash```


## Part#4
### Exécuter une commande dans le conteneur django_app pour créer une nouvelle application app_blog
```docker-compose run django_app sh -c "django-admin startapp app_blog ."```

### Ouvrir un shell interactif dans le conteneur django_app
```docker exec -it django_app sh```

### Exécuter des tâches Celery pour ajouter 2 et 2 de manière asynchrone
```python manage.py shell
from app_blog.tasks import add
add.delay(2, 2)```


## Part#5
### Se connecter à psadmin en utilisant les paramètres spécifiés
http://localhost:5051/

```
- PGADMIN_DEFAULT_EMAIL=user@domain.com
- PGADMIN_DEFAULT_PASSWORD=SuperSecret
- DB_HOST=db
- DB_NAME=devdb
- DB_USER=devuser
- DB_PASS=devpass
```
