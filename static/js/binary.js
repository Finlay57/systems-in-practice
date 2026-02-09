function convertBinary() {
    const input = document.getElementById("binaryInput").value.trim();
    const resultEl = document.getElementById("result");

    // Validate: binary can only contain 0s and 1s
    if (!/^[01]+$/.test(input)) {
        resultEl.textContent = "Please enter a valid binary number (0s and 1s only).";
        resultEl.style.color = "red";
        return;
    }

    // Convert binary to decimal
    const decimalValue = parseInt(input, 2);

    resultEl.textContent = `Decimal value: ${decimalValue}`;
    resultEl.style.color = "black";
}
