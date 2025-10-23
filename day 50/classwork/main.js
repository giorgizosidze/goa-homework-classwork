// 1 davaleba
//  console.log() — ეს ბრძანება გამოიყენება იმისთვის, რომ რაიმე ინფორმაცია გამოვიტანოთ კონსოლში.
// მაგალითად, შეგვიძლია გამოვიტანოთ ტექსტი, რიცხვი ან ცვლადის მნიშვნელობა.

console.log('Hello world!')


// 2 davaleba
// var — ძველი მეთოდია. ქმნის ცვლადს მთელ პროგრამის ფარგლებზე (global scope).
// let — ქმნის ცვლადს კონკრეტული ბლოკის ფარგლებში (block scope), ანუ ფიგურული ფრჩხილებიდან გარეთ არ ჩანს.
// const — ქმნის მუდმივ ცვლადს, რომლის მნიშვნელობა შეცვლადი აღარ არის.


// 3 davaleba

let name = "Giorgi";
let lastName = "Zosidze";
let age = 15;


// 4 davaleba
// განსხვავება let-სა და const-ს შორის:
// let-ით შექმნილი ცვლადის მნიშვნელობა შეგვიძლია შევცვალოთ.
// const-ით შექმნილი ცვლადის მნიშვნელობა შეცვლადი აღარ არის (მუდმივი მნიშვნელობა აქვს).


// 5 davaleba

let myAge = 15;     
myAge = 16;         
console.log(myAge);



// 6 davaleba 
// const — შეუცვლელი ცვლადის შესაქმნელად ვიყენებთ const-ს.
// ამ ცვლადის მნიშვნელობა შეცვლადი აღარ იქნება.
const myName = "Giorgi";
console.log(myName); 


// 7 davaleba

let Name = "Giorgi";
let aGe = 15;


console.log(Name, age); 


console.log("My name is " + Name + " and I am " + aGe + " years old.");


console.log(`My name is ${Name} and I am ${aGe} years old.`);


// 8 davaleba 

console.log("Hello, world!");             
console.log(25 + 30);                     
console.log(true);                        
console.log(["apple", "banana", "kiwi"]); 
console.log({name: "Giorgi", age: 15});   



// 9 davaleba

let country = "Georgia";
let city = "Tbilisi";
let population = 1000000;
let isCapital = true;
let temperature = 25.6;
let favoriteColor = "blue";
let numberOfFriends = 5;
let hasPet = false;
let petName = "Batu";
let year = 2025;

console.log(country, city, population, isCapital, temperature, favoriteColor, numberOfFriends, hasPet, petName, year);


// 10 davaleba



// მაგალითები

// 1 magaliti
var x = 10;
console.log(x); 0

// 2 magaliti
var x = 20; 
console.log(x); 

// 3 magaliti
if (true) {
  var y = 5; 
}
console.log(y);

// 4 magaliti
if (true) {
  let z = 7;
}

// 5 magaliti
var message = "Hello";
message = "Hi"; 
console.log(message);
