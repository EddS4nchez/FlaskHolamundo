import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo con Flask"

# Ejecutar la aplicación
if __name__ == "__main__":
    # Esto permite que Railway asigne el puerto automáticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
