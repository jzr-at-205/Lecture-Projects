// The following is filler code for a program test.

function square(num)
{
    return num * num;
}

// making a class in Js
class Student {
    constructor(name, grade, id)
    {
        this.name = name;
        this.grade = grade;
        this.id = id;
    }

    // method to display the student details
    display_info()
    {
        console.log("Name: " + this.name);
        console.log("Grade: " + this.grade);
        console.log("ID: " + this.id);
    }


}

// creating an object of the class
const stud1 = new Student("Jonn", 'A', 552226);
stud1.display_info();

// pythagorean theorem
// a^2 + b^2 = c^2
const prompt=require("prompt-sync")({sigint:true}); 

//let name = prompt("What's your name");
//console.log("hello"+name+"!");


function pythagorean(a, b)
{
    return Math.sqrt(square(a) + square(b));
}

console.log("Hello, World!");
var my_age = 19;
console.log(my_age);

var a = prompt("Enter side a: ");
var b = prompt("Enter side b: ");
var c = pythagorean(a, b);

// displaying missing side
console.log("Hypotenuse is: " + c.toFixed(2));