# Use an official Python runtime as a parent image
# Au début, on se sert d'une image de base, cela peut être une image contenant les libs d'un langage, voire carrément une distrib linux
FROM python:2.7-slim

# Set the working directory to /app
# ici on définit que notre répertoire de travail sera /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# Lorsque l'on construit notre application, on indique que ce même répertoire "app" sera ajouté dans notre conteneur
ADD . /app

# Install any needed packages specified in requirements.txt
# On spécifie ici, des éléments à installer depuis un fichier texte spécifique.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 3000 available to the world outside this container
# On rend disponible le port 3000 pour notre conteneur
EXPOSE 3000

# Define environment variable
# on crée une variable d'environnement
ENV NAME World

# Run app.py when the container launches
# on lance une commande pour démarrer notre application :)
CMD ["python", "app.py"]