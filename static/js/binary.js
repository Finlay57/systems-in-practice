function convertBinaryToDecimal() {
    const input = document.getElementById("binaryInput").value.trim();
    const resultEl = document.getElementById("result");

    if (!/^[01]+$/.test(input)) {
        resultEl.textContent = "Please enter a valid binary number (0s and 1s only).";
        resultEl.style.color = "red";
        return;
    }

    const decimalValue = parseInt(input, 2);
    resultEl.textContent = `Decimal value: ${decimalValue}`;
    resultEl.style.color = "black";
}

function convertDecimalToBinary() {
    const input = document.getElementById("decimalInput").value.trim();
    const resultEl = document.getElementById("result");

    if (input === "" || Number(input) < 0) {
        resultEl.textContent = "Please enter a valid non-negative decimal number.";
        resultEl.style.color = "red";
        return;
    }

    const binaryValue = Number(input).toString(2);
    resultEl.textContent = `Binary value: ${binaryValue}`;
    resultEl.style.color = "black";
}
