import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                if num2 == 0:
                    error = "Error: División entre cero"
                else:
                    resultado = num1 / num2
            else:
                error = "Operación no válida."
        except ValueError:
            error = "Por favor ingresa valores numéricos válidos."

    return render_template("index.html", resultado=resultado, error=error)

# 🚀 Código correcto para producción (Railway/Render/Heroku)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que da Railway
    app.run(host="0.0.0.0", port=port)
