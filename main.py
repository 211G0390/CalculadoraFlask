from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
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
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error: División entre cero"
        except ValueError:
            resultado = "Por favor, ingresa valores numéricos válidos."

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # ← Usa el puerto que Railway asigna
    app.run(host="0.0.0.0", port=port)
