
// 3 davaleba


let a = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let b = Number(prompt("შეიყვანე მეორე რიცხვი:"));

if (a === b) {
  console.log("რიცხვები ტოლია");
} else {
  console.log("რიცხვები არ არის ტოლი");

  if (a > b) {
    console.log(a + " არის მეტი, ხოლო " + b + " ნაკლებია");
  } else {
    console.log(b + " არის მეტი, ხოლო " + a + " ნაკლებია");
  }
}
