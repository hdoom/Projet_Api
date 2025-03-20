# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
#COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install python-opensky-api
RUN pip install python-dotenv
#RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application s'exécute (si nécessaire)
# EXPOSE 8000

# Définir la commande de démarrage
CMD ["python", "main.py"]