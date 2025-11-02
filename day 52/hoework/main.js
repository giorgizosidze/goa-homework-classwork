// 1 davaleba


// alert() - გამოიყენება ეკრანზე გაფრთხილების ან შეტყობინების გამოყვანისთვის.
// ის აჩენს პატარა ფანჯარას OK ღილაკით


// 2 davaleba


//prompt() - გამოიყენება მომხმარებლისგან ინფორმაციის მისაღებად.
// აჩენს ფანჯარას, სადაც მომხმარებელი რაღაც ტექსტს ან რიცხვს შეიყვანს



// 4 davaleba


alert("hello world");


// 5 davaleba


let num1 = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let num2 = Number(prompt("შეიყვანე მეორე რიცხვი:"));

console.log( num1 + num2);
console.log( num1 - num2);
console.log( num1 * num2);
console.log( num1 / num2);
console.log( num1 % num2);



// 6 davaleba


let age = Number(prompt("შეიყვანე შენი ასაკი:"));

if (age >= 18) {
    alert("სრულწლოვანი ხარ ");
} else {
    alert("არ ხარ სრულწლოვანი ");
}



// 7 davaleba


let a = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let b = Number(prompt("შეიყვანე მეორე რიცხვი:"));

if (a > 0) {
    console.log(a, "დადებითია");
} else {
    console.log(a, "უარყოფითია");
}

if (b > 0) {
    console.log(b, "დადებითია");
} else {
    console.log(b, "უარყოფითია");
}




// 8 davaleba

\\
let x = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let y = Number(prompt("შეიყვანე მეორე რიცხვი:"));

if (symbol === "+") {
    console.log(x + y);
} else if (symbol === "-") {
    console.log(x - y);
} else if (symbol === "*") {
    console.log(x * y);
} else if (symbol === "/") {
    console.log(x / y);
} else if (symbol === "%") {
    console.log(x % y);
} else {
    console.log("შეყვანილი სიმბოლო არასწორია!");
}
