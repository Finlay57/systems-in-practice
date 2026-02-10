from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/binary", methods=["GET", "POST"])
def binary():
    # Decimal → Binary
    d2b_result = None
    d2b_steps = []
    d2b_error = None
    decimal_input = None

    # Binary → Decimal
    b2d_result = None
    b2d_steps = []
    b2d_error = None
    binary_input = None

    if request.method == "POST":

        # ---------- Decimal → Binary ----------
        if "decimal" in request.form:
            decimal_input = request.form.get("decimal", "").strip()

            if not decimal_input:
                d2b_error = "Please enter a decimal number."
            elif not decimal_input.isdigit():
                d2b_error = "Decimal input must be a non-negative integer."
            else:
                n = int(decimal_input)

                if n == 0:
                    d2b_result = "0"
                    d2b_steps.append("0 in binary is 0")
                else:
                    binary_digits = []

                    while n > 0:
                        remainder = n % 2
                        d2b_steps.append(
                            f"{n} ÷ 2 = {n // 2} remainder {remainder}"
                        )
                        binary_digits.append(str(remainder))
                        n //= 2

                    binary_digits.reverse()
                    d2b_result = "".join(binary_digits)
                    d2b_steps.append(
                        f"Read remainders from bottom to top → {d2b_result}"
                    )

        # ---------- Binary → Decimal ----------
        if "binary" in request.form:
            binary_input = request.form.get("binary", "").strip()

            if not binary_input:
                b2d_error = "Please enter a binary number."
            elif not all(bit in "01" for bit in binary_input):
                b2d_error = "Binary input may only contain 0s and 1s."
            else:
                decimal_value = 0
                power = len(binary_input) - 1

                for bit in binary_input:
                    contribution = int(bit) * (2 ** power)
                    b2d_steps.append(
                        f"{bit} × 2^{power} = {contribution}"
                    )
                    decimal_value += contribution
                    power -= 1

                b2d_result = decimal_value
                b2d_steps.append(f"Total = {decimal_value}")

    return render_template(
        "binary.html",
        d2b_result=d2b_result,
        d2b_steps=d2b_steps,
        d2b_error=d2b_error,
        decimal_input=decimal_input,
        b2d_result=b2d_result,
        b2d_steps=b2d_steps,
        b2d_error=b2d_error,
        binary_input=binary_input
    )


@app.route("/api/fact")
def api_fact():
    return jsonify({
        "fact": "Computers store all data as binary, but humans are much better at base 10."
    })

if __name__ == "__main__":
    app.run(debug=True)
