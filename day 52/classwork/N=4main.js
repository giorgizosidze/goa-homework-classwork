// 4 davaleba

let symbol = prompt("შეიყვანე მათემატიკური სიმბოლო (+, -, *, /, %):");
let num1 = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let num2 = Number(prompt("შეიყვანე მეორე რიცხვი:"));

let result;

if (symbol === "+") {
  result = num1 + num2;
} else if (symbol === "-") {
  result = num1 - num2;
} else if (symbol === "*") {
  result = num1 * num2;
} else if (symbol === "/") {
  result = num1 / num2;
} else if (symbol === "%") {
  result = num1 % num2;
} else {
  alert("არასწორი სიმბოლოა!");
}

alert("შედეგი არის: " + result);
