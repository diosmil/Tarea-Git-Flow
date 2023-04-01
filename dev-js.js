
let operand1 = "";
let operand2 = "";
let operator = "";
let result = "";

function addNumber(number) {
    if (operator === "") {
        operand1 += number;
        document.getElementById("result").value = operand1;
    } else {
        operand2 += number;
        document.getElementById("result").value = operand2;
    }
}

function addOperator(op) {
    operator = op;
}

function calculate() {
    switch (operator) {
        case "+":
            result = parseFloat(operand1) + parseFloat(operand2);
            break;
        case "-":
            result = parseFloat(operand1) - parseFloat(operand2);
            break;
        case "*":
            result = parseFloat(operand1) * parseFloat(operand2);
            break;
        case "/":
            result = parseFloat(operand1) / parseFloat(operand2);
            break;
        default:
            break;
    }
    document.getElementById("result").value = result;
}

function clearScreen() {
    operand1 = "";
    operand2 = "";
    operator = "";
    result = "";
    document.getElementById("result").value = "";
}
