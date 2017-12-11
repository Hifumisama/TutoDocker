from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        # On demande à chaque fois que l'on atterit sur la route, d'incrémenter une valeur.
        visits = redis.incr("counter")
    except RedisError:
        # Sauf si redis renvoie une erreur :D
        visits = "<i>cannot connect to Redis, counter disabled</i>"
        # On renvoie du html (tout con en effet XD, contenant les valeurs des variables que l'on veut).
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
        # Ici on rend l'HTML avec le contenu récupéré de nos variables (of course !  \_o_/  ).
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    # on lance sur le serveur, avec pour adresse 0.0.0.0, ("probablement" local donc), et sur le port 3000.
    app.run(host='0.0.0.0', port=3000)

