from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/binary", methods=["GET", "POST"])
def binary():
    result = None
    steps = []

    if request.method == "POST":
        conversion_type = request.form.get("conversion")

        # Binary -> Decimal
        if conversion_type == "bin_to_dec":
            binary = request.form.get("binary")

            decimal_value = 0
            power = len(binary) - 1

            for bit in binary:
                decimal_value += int(bit) * (2 ** power)
                steps.append(f"{bit} × 2^{power}")
                power -= 1

            result = decimal_value

        # Decimal -> Binary
        elif conversion_type == "dec_to_bin":
            decimal = int(request.form.get("decimal"))
            n = decimal

            if n == 0:
                steps.append("0 ÷ 2 = 0 remainder 0")
                result = "0"
            else:
                binary_digits = []

                while n > 0:
                    remainder = n % 2
                    steps.append(f"{n} ÷ 2 = {n // 2} remainder {remainder}")
                    binary_digits.append(str(remainder))
                    n //= 2

                result = "".join(reversed(binary_digits))

    return render_template(
        "binary.html",
        result=result,
        steps=steps
    )



@app.route("/api/fact")
def api_fact():
    return jsonify({
        "fact": "Computers store all data as binary, but humans are much better at base 10."
    })

if __name__ == "__main__":
    app.run(debug=True)
