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

