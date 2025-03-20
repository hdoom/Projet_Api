# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires pour git
RUN apt-get update && apt-get install -y git

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install python-dotenv
RUN pip install git+https://github.com/openskynetwork/opensky-api.git#subdirectory=python

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application s'exécute (si nécessaire)
# EXPOSE 8000

# Définir la commande de démarrage
CMD ["python", "main.py"]