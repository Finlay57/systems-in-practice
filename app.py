from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/binary")
def binary_converter():
    return render_template("binary.html")

@app.route("/api/fact")
def api_fact():
    return jsonify({
        "fact": "Computers store all data as binary, but humans are much better at base 10."
    })

if __name__ == "__main__":
    app.run(debug=True)
